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
    memberdata = getToolByName(portal, 'portal_memberdata')
    all_props = memberdata.propertyIds()
    membership = getToolByName(portal, 'portal_membership')
    openid_name, openid = getPASPlugin(portal)
    all_registrations = openid.store.getAllRegistrations()

    users = membership.searchForMembers()
    legacy_user_ids = dict([
        (user.getId(), encodeIdentityURL(user.getId()))
        for user in users
        if (user.getId().startswith("http:") or \
            user.getId().startswith("https:"))
    ])
    # Fix the short window of badly-encoded usernames
    legacy_user_ids.update(dict([
        (user.getId(), encodeIdentityURL(unquote_plus(user.getId())))
        for user in users
        if (user.getId().startswith("http%3A") or \
            user.getId().startswith("https%3A"))
    ]))

    for legacy_user_id, new_user_id in legacy_user_ids.items():
        # Copy registration from old identity_url to new encoded ID
        all_registrations[new_user_id] = all_registrations[legacy_user_id]
        legacy_member = membership.getMemberById(legacy_user_id)
        new_member = membership.getMemberById(new_user_id)
        properties = dict([
            (property_id, legacy_member.getProperty(property_id))
            for property_id in all_props
        ])
        new_member.setMemberProperties(properties)
        memberdata.deleteMemberData(legacy_user_id)
