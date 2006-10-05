from StringIO import StringIO
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.Extensions.utils import install_subskin
from Products.PluggableAuthService.interfaces.plugins import IExtractionPlugin
from plone.openid.interfaces import IOpenIdExtractionPlugin
from plone.app.openid.config import GLOBALS

def listOpenIdPlugins(portal):
    acl=getToolByName(portal, "acl_users")
    plugins=acl.plugins.listPlugins(IExtractionPlugin)
    plugins=[plugin[0] for plugin in plugins 
            if IOpenIdExtractionPlugin.providedBy(plugin[1])]
    return plugins


def hasOpenIdPlugin(portal):
    return portal.restrictedTraverse("acl_users/@@openid").ShowOpenIdLogin()


def createOpenIdPlugin(portal, out):
    print >>out, "Adding an OpenId plugin"
    acl=getToolByName(portal, "acl_users")
    acl.manage_addProduct["plone.openid"].addOpenIdPlugin(
            id="openid", title="OpenId authentication plugin")


def activatePlugin(portal, out, plugin):
    acl=getToolByName(portal, "acl_users")
    plugin=getattr(acl, plugin)
    interfaces=plugin.listInterfaces()

    activate=[]

    for info in acl.plugins.listPluginTypeInfo():
        interface=info["interface"]
        interface_name=info["id"]
        if plugin.testImplements(interface):
            activate.append(interface_name)
            print >>out, "Activating interface %s for plugin %s" % \
                    (interface_name, info["title"])

    plugin.manage_activateInterfaces(activate)


def install(self):
    out = StringIO()
    install_subskin(self, out, GLOBALS)

    if not hasOpenIdPlugin(self):
        createOpenIdPlugin(self, out)
        activatePlugin(self, out, "openid")
    return out.getvalue()


def uninstall(self, reinstall):
    if reinstall:
        return

    acl=getToolByName(self, "acl_users")
    for plugin in listOpenIdPlugins(self):
        acl._delObject(plugin)
