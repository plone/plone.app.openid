import unittest
from plone.app.openid.tests.base import OpenIdTestCase

class TestOpenIdView(OpenIdTestCase):
    def test_DefaultConfig(self):
        view=self.view
        self.assertEquals(view.ShowOpenIdLogin(), False)
        self.assertEquals(view.ShowStandardLogin(), True)

    def test_Install(self):
        self.portal.portal_quickinstaller.installProduct("plone.app.openid")
        view=self.view
        self.assertEquals(view.ShowOpenIdLogin(), True)
        self.assertEquals(view.ShowStandardLogin(), True)




def test_suite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestOpenIdView))
    return suite

