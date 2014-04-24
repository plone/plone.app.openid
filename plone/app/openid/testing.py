# -*- coding: utf-8 -*-

from zope.configuration import xmlconfig

from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing.layers import IntegrationTesting


class PloneAppOpenidLayer(PloneSandboxLayer):

    def setUpZope(self, app, configurationContext):
        import plone.openid
        self.loadZCML(package=plone.openid)
        z2.installProduct(app, 'plone.openid')
        z2.installProduct(app, 'plone.app.openid')
        import plone.app.openid
        xmlconfig.file(
            'configure.zcml',
            plone.app.openid,
            context=configurationContext)

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'plone.app.openid')

PLONEAPPOPENID_FIXTURE = PloneAppOpenidLayer()

PLONEAPPOPENID_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONEAPPOPENID_FIXTURE,),
    name="PloneAppCollectionLayer:Integration")
