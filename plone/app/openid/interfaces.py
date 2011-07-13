from Products.PluggableAuthService.interfaces.events import IUserLoggedInEvent


class IOpenIDUserLoggedInEvent(IUserLoggedInEvent):
    """A user successfully authenticated against an OpenID server.
    """
