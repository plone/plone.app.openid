from Products.PloneTestCase import PloneTestCase
PloneTestCase.setupPloneSite()

class OpenIdTestCase(PloneTestCase.PloneTestCase):
    @property
    def pas(self):
        return self.portal.acl_users

    @property
    def view(self):
        return self.pas.restrictedTraverse("@@openid")


class OpenIdFunctionalTestCase(PloneTestCase.Functional, OpenIdTestCase):
    pass
