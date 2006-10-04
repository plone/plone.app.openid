from zope.interface import Interface

class IOpenIdView(Interface):
    """
    The OpenId view exposes information about the authentication options
    and some OpenId settings.
    """

    def ShowOpenIdLogin():
        """
        Indicate if an OpenId login option should be shown.
        """

    def ShowStandardLogin():
        """
        Indicate if a standard username/password login option should be shown.
        """

