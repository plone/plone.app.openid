This package integrates the OpenID authentication support from the
'plone.openid' package into a Plone site.

Requirements

    Plone's OpenID Authentication Support has a few requirements to be able to function:

    1. The 'plone.openid' package must be installed in your Zope instance.
       (Plone 3.0 and later include this package by default)

    2. The 'python-openid' python package must be installed in your python
       path. This package can be downloaded from the 
       "Python Cheese Shop":http://cheeseshop.python.org package directory,
       or installed using the easy_install command::

        easy_install python-openid

    3. The 'python-urljr' python package must be installed in your python
       path. This package can be downloaded from same aforementioned site or
       installed via the easy_install command::

        easy_install python-urljr

Features

    This product makes three modifications to a Plone site:

    1. an OpenID PAS plugin instance is created

    2. the login form is replaced with a form which also supports 
       authentication via OpenID identity URLs.

    3. it adds a new login portlet type for OpenID identity URL based
       logins and adds this to the left column.

    Both the login form and the portlet check the current PAS configuration to
    see if OpenID login should be offered.

