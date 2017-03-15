# -*- coding: utf-8 -*-
from plone.app.openid.testing import PLONEAPPOPENID_INTEGRATION_TESTING
from Products.PluggableAuthService.interfaces import plugins as plugin_ifaces

import unittest2 as unittest


class TestOpenIdView(unittest.TestCase):

    layer = PLONEAPPOPENID_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    @property
    def pas(self):
        return self.portal.acl_users

    @property
    def pas_info(self):
        return self.pas.restrictedTraverse('@@pas_info')

    def test_DefaultConfig(self):
        pas_info = self.pas_info
        self.assertEqual(pas_info.hasOpenIDExtractor(), False)
        self.assertEqual(pas_info.hasLoginPasswordExtractor(), True)

    def test_OpenIdInstalled(self):
        self.portal.portal_setup.runAllImportStepsFromProfile(
            'profile-plone.app.openid:default')
        pas_info = self.pas_info
        self.assertEqual(pas_info.hasOpenIDExtractor(), True)
        self.assertEqual(pas_info.hasLoginPasswordExtractor(), True)

    def testOnlyOpenIdInstalled(self):
        plugins = self.pas.plugins.listPlugins(plugin_ifaces.IExtractionPlugin)
        for (id, plugin) in plugins:
            if plugin_ifaces.ILoginPasswordExtractionPlugin.providedBy(plugin):
                plugin.manage_activateInterfaces(interfaces=())
        self.portal.portal_setup.runAllImportStepsFromProfile(
            'profile-plone.app.openid:default')

        pas_info = self.pas_info
        self.assertEqual(pas_info.hasOpenIDExtractor(), True)
        self.assertEqual(pas_info.hasLoginPasswordExtractor(), False)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestOpenIdView))
    return suite
