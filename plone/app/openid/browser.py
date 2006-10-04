from zope.interface import implements
from Products import Five
from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.utils import implementedBy
from Products.PluggableAuthService.interfaces.plugins \
        import IExtractionPlugin, ILoginPasswordExtractionPlugin
from plone.openid.interfaces import IOpenIdExtractionPlugin
from interfaces import IOpenIdView

class OpenIdView(Five.BrowserView):
    """Expose OpenId related information to templates.
    """
    implements(IOpenIdView)

    def __init__(self, context, request):
        Five.BrowserView.__init__(self, context, request)
        acl=getToolByName(context, "acl_users")
        plugins=acl.plugins.listPlugins(IExtractionPlugin)

        self.normal=False
        self.openid=False

        for plugin in plugins:
            if ILoginPasswordExtractionPlugin.providedBy(plugin[1]):
                self.normal=True
            if IOpenIdExtractionPlugin.providedBy(plugin[1]):
                self.openid=True


    def ShowOpenIdLogin(self):
        return self.openid


    def ShowStandardLogin(self):
        return self.normal



