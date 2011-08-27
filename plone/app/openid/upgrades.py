from urllib import unquote_plus

from zope.app.component.hooks import getSite

from Products.CMFCore.utils import getToolByName

from plone.openid.util import encodeIdentityURL, getPASPlugin
from plone.openid.upgrades import urlencode_usernames


def update_property_usernames(context):
    """This upgrade step is intended to ensure that any current user profiles
    are updated to use URL-encoded OpenID identity URLs, to avoid traversal
    issues when Plone encounters a / in the URL.
    """
    portal = getSite()
    acl = getToolByName(portal, 'acl_users')
    memberdata = getToolByName(portal, 'portal_memberdata')
    all_properties = memberdata.propertyIds()
    membership = getToolByName(portal, 'portal_membership')
    openid_name, openid = getPASPlugin(portal)
    all_registrations = openid.store.getAllRegistrations()

    # We use searchUsers to get as many records as possible
    # vs. searchForMembers, which only returns members for the
    # active user
    users = dict([(user_info['id'], user_info)
                  for user_info in acl.searchUsers()])
    legacy_user_ids = dict([
        (user_id, encodeIdentityURL(user_id))
        for user_id in users
        if (user_id.startswith("http:") or \
            user_id.startswith("https:"))
    ])

    # Fix the short window of badly-encoded usernames
    legacy_user_ids.update(dict([
        (user_id, encodeIdentityURL(unquote_plus(user_id)))
        for user_id in users
        if (user_id.startswith("http%3A") or \
            user_id.startswith("https%3A"))
    ]))

    # Accumulate multiple legacy usernames pointing to the same encoded value
    encoded_legacy = {}
    for legacy_user_id, new_user_id in legacy_user_ids.items():
        encoded_legacy.setdefault(new_user_id, []).append(legacy_user_id)

    for new_id, legacy_ids in encoded_legacy.items():
        sreg = {}
        properties = {}

        for legacy_id in legacy_ids:
            # Update with each legacy dataset
            for sreg_id, sreg_val in all_registrations.get(legacy_id,
                                                           {}).items():
                if sreg_val:
                    sreg[sreg_id] = sreg_val

            # Use getUserById instead of getMemberById,
            # so that we can access properties for inactive members
            legacy_user = acl.getUserById(legacy_id)
            if legacy_user is not None:
                # Usual case, we found a User
                recorded_properties = dict([
                    (property_id, legacy_user.getProperty(property_id))
                    for property_id in all_properties
                ])
            else:
                # We have no User, only recourse is to try a known plugin
                if users[legacy_id].get('pluginid') == 'mutable_properties':
                    recorded_properties = get_mutable_properties(portal,
                                                                 legacy_id)
                    if recorded_properties is None:
                        # Ah well, we tried
                        continue

            # Accumulate properties
            for property_id, property_val in recorded_properties.items():
                if property_val:
                    properties[property_id] = property_val
                elif hasattr(legacy_user, property_id) and \
                     getattr(legacy_user, property_id):
                    properties[property_id] = getattr(legacy_user, property_id)
            # Destroy all legacy property entries
            if hasattr(memberdata, 'deleteMemberData'):
                memberdata.deleteMemberData(legacy_id)

        if sreg and properties:
            # Create new OpenID user record
            openid.store.storeSimpleRegistration(new_id, sreg)
            new_member = membership.getMemberById(new_id)
            # Update newly-created member with accumulated properties
            new_member.setMemberProperties(properties)
            for property_id, property_val in properties.items():
                if hasattr(new_member, property_id):
                    setattr(new_member, property_id, property_val)

def get_mutable_properties(context, legacy_id):
    # Try to resurrect info directly from the plugin
    from Products.PlonePAS.interfaces.plugins import IMutablePropertiesPlugin
    from Products.PluggableAuthService.interfaces.plugins import \
         IPropertiesPlugin
    mp_name, mutable = getPASPlugin(context,
                                    plugin_type=IPropertiesPlugin,
                                    provides=IMutablePropertiesPlugin)
    if mp_name is None:
        return None

    return mutable._storage.get(legacy_id, None)
