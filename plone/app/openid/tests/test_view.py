import unittest
from plone.app.openid.tests.base import OpenIdTestCase
from Products.PluggableAuthService.interfaces.plugins \
        import IExtractionPlugin, ILoginPasswordExtractionPlugin

class TestOpenIdView(OpenIdTestCase):
    def test_DefaultConfig(self):
        view=self.view
        self.assertEquals(view.ShowOpenIdLogin(), False)
        self.assertEquals(view.ShowStandardLogin(), True)

    def test_OpenIdInstalled(self):
        self.portal.portal_quickinstaller.installProduct("plone.app.openid")
        view=self.view
        self.assertEquals(view.ShowOpenIdLogin(), True)
        self.assertEquals(view.ShowStandardLogin(), True)

    def testOnlyOpenIdInstalled(self):
        plugins=self.pas.plugins.listPlugins(IExtractionPlugin)
        for (id, plugin) in plugins:
            if ILoginPasswordExtractionPlugin.providedBy(plugin):
                plugin.manage_activateInterfaces(interfaces=())
        self.portal.portal_quickinstaller.installProduct("plone.app.openid")

        view=self.view
        self.assertEquals(view.ShowOpenIdLogin(), True)
        self.assertEquals(view.ShowStandardLogin(), False)


def test_suite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestOpenIdView))
    return suite

