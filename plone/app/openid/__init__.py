# -*- coding: utf-8 -*-
from AccessControl import ModuleSecurityInfo
from zope.i18nmessageid import MessageFactory


PloneMessageFactory = MessageFactory('plone')
ModuleSecurityInfo('plone.app.openid').declarePublic('PloneMessageFactory')  # noqa
