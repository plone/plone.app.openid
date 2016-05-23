# -*- coding: utf-8 -*-
from plone.app.openid.portlets.login import Assignment as LoginAssignment
from plone.openid.plugins.oid import addOpenIdPlugin
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from Products.CMFCore.utils import getToolByName
from Products.PlonePAS.browser.info import PASInfoView
from StringIO import StringIO
from zope.component import getMultiAdapter
from zope.component import queryUtility


def hasOpenIdPlugin(portal):
    pas_info = PASInfoView(portal, None)
    return pas_info.hasOpenIDExtractor()


def createOpenIdPlugin(portal, out):
    print >>out, 'Adding an OpenId plugin'  # noqa
    acl = getToolByName(portal, 'acl_users')
    addOpenIdPlugin(acl, id='openid', title='OpenId authentication plugin')


def activatePlugin(portal, out, plugin):
    acl = getToolByName(portal, 'acl_users')
    plugin = getattr(acl, plugin)

    activate = []

    for info in acl.plugins.listPluginTypeInfo():
        interface = info['interface']
        interface_name = info['id']
        if plugin.testImplements(interface):
            activate.append(interface_name)
            print >>out, 'Activating interface {0} for plugin {1}'.format(
                interface_name, info['title'])  # noqa

    plugin.manage_activateInterfaces(activate)


def addLoginPortlet(portal, out):
    leftColumn = queryUtility(
        IPortletManager, name=u'plone.leftcolumn', context=portal)
    if leftColumn is not None:
        left = getMultiAdapter((portal, leftColumn,),
                               IPortletAssignmentMapping, context=portal)
        if u'openid-login' not in left:
            print >>out, 'Adding OpenID login portlet to the left column'  # noqa
            left[u'openid-login'] = LoginAssignment()


def importVarious(context):
    # Only run step if a flag file is present (e.g. not an extension profile)
    if context.readDataFile('openid-pas.txt') is None:
        return

    site = context.getSite()
    out = StringIO()
    if not hasOpenIdPlugin(site):
        createOpenIdPlugin(site, out)
        activatePlugin(site, out, 'openid')

    addLoginPortlet(site, out)
