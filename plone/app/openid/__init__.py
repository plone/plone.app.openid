from Products.GenericSetup.interfaces import EXTENSION
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.GenericSetup import profile_registry
from plone.openid.config import HAS_OPENID

def initialize(context):
    if HAS_OPENID:
        profile_registry.registerProfile(
                name="default",
                title="OpenID authentication support",
                description="Adds support for authenticating with OpenID credentials in a Plone site",
                path="profiles/default",
                product="plone.app.openid",
                profile_type=EXTENSION,
                for_=IPloneSiteRoot)



