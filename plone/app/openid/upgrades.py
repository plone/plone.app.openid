from urllib import quote_plus

from zope.app.component.hooks import getSite

from Products.CMFCore.utils import getToolByName
from Products.PlonePAS.interfaces.plugins import IMutablePropertiesPlugin
from Products.PluggableAuthService.interfaces.plugins import IPropertiesPlugin

from plone.openid.util import getPASPlugin

def update_property_usernames(context):
    """This upgrade step is intended to ensure that any current user profiles
    are updated to use URL-encoded OpenID identity URLs, to avoid traversal
    issues when Plone encounters a / in the URL.
    """
    portal = getSite()
    acl = getToolByName(portal, 'acl_users')
    plugin_name, property_plugin = \
        getPASPlugin(acl,
                     plugin_type=IPropertiesPlugin,
                     provides=IMutablePropertiesPlugin)
    user_ids = [
        user_id
        for user_id in property_plugin._storage.keys()
        if (user_id.startswith("http:") or user_id.startswith("https:"))
    ]
    for user_id in user_ids:
        user = acl.getUserById(user_id)
        sheet = property_plugin.getPropertiesForUser(user)
        # The following is a bit of a hack
        old_getId = user.getId
        user.getId = lambda: quote_plus(user_id)
        property_plugin.setPropertiesForUser(user, sheet)
        property_plugin.deleteUser(user_id)
        user.getId = old_getId
