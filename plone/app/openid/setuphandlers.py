# -*- coding: utf-8 -*-
from plone.app.openid.portlets.login import Assignment as LoginAssignment
from plone.openid.plugins.oid import addOpenIdPlugin
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletType
from Products.CMFCore.utils import getToolByName
from Products.PlonePAS.browser.info import PASInfoView
from StringIO import StringIO
from zope.component import getMultiAdapter
from zope.component import getSiteManager
from zope.component import queryUtility
from zope.component.interfaces import IComponentRegistry

import logging


logger = logging.getLogger('plone.app.openid')
PROFILE_ID = 'plone.app.openid:default'


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


def removeOpenIdPlugin(portal):
    if hasOpenIdPlugin(portal):
        acl = getToolByName(portal, 'acl_users')
        acl._delObject('openid')
        logger.info('Removed openid plugin from acl_users.')


def addLoginPortlet(portal, out):
    leftColumn = queryUtility(
        IPortletManager, name=u'plone.leftcolumn', context=portal)
    if leftColumn is not None:
        left = getMultiAdapter((portal, leftColumn,),
                               IPortletAssignmentMapping, context=portal)
        if u'openid-login' not in left:
            print >>out, 'Adding OpenID login portlet to the left column'  # noqa
            left[u'openid-login'] = LoginAssignment()


def removeLoginPortlet(portal):
    leftColumn = queryUtility(
        IPortletManager, name=u'plone.leftcolumn', context=portal)
    if leftColumn is not None:
        left = getMultiAdapter((portal, leftColumn,),
                               IPortletAssignmentMapping, context=portal)
        if u'openid-login' in left:
            del left[u'openid-login']
            logger.info('Removed OpenID login portlet from the left column')


def importVarious(context):
    site = getToolByName(context, 'portal_url').getPortalObject()
    out = StringIO()
    if not hasOpenIdPlugin(site):
        createOpenIdPlugin(site, out)
        activatePlugin(site, out, 'openid')

    addLoginPortlet(site, out)


def registerPortletAddview(context):
    portal = getToolByName(context, 'portal_url').getPortalObject()
    sm = getSiteManager(portal)
    if sm is None or not IComponentRegistry.providedBy(sm):
        # plone.app.portlets.exportimport.portlets has this same check.
        logger.info('Cannot register portlet addview - no site manager found.')
        return
    if queryUtility(IPortletType, name=''):
        # For a few years we have registered our portlet with an empty string
        # as add view.  This is wrong.
        sm.unregisterUtility(provided=IPortletType, name='')
        logger.info('Unregistered portlet type with empty addview.')
    addview = 'portlets.OpenIDLogin'
    if queryUtility(IPortletType, name=addview) is None:
        # Apply our default portlets.xml.
        context.runImportStepFromProfile(PROFILE_ID, 'portlets')
        logger.info('Applied our portlets.xml to register portlet '
                    'with correct addview.')


def uninstall(context):
    portal = getToolByName(context, 'portal_url').getPortalObject()
    removeOpenIdPlugin(portal)
    removeLoginPortlet(portal)
