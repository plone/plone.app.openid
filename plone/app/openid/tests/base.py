from Products.PloneTestCase import PloneTestCase
PloneTestCase.setupPloneSite()

class OpenIdTestCase(PloneTestCase.PloneTestCase):
    @property
    def pas(self):
        return self.portal.acl_users

    @property
    def pas_info(self):
        return self.pas.restrictedTraverse("@@pas_info")


class OpenIdFunctionalTestCase(PloneTestCase.Functional, OpenIdTestCase):
    pass
