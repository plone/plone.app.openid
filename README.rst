Overview
========

This package makes Plone a complete OpenID consumer, allowing people
to authenticate in a site using their OpenID identity. It relies on the
plone.openid_ package to implement authentication of identities and
needs an external session management plugin such as plone.session_ to
add session management.

You also need version 2.2.x of the python-openid_ package from JanRain. If this
package is not installed you will not be able to install OpenID support in
Plone.

.. _plone.openid: http://pypi.python.org/pypi/plone.openid
.. _plone.session: http://pypi.python.org/pypi/plone.session
.. _python-openid: http://pypi.python.org/pypi/python-openid/


Installation
============

If all requirements have been installed you should see an *OpenID
Authentication Support* appear in the *Add/Remove Products* page in
the Plone site setup screen. Installing the OpenID authentication
support will do several things:

 * The PAS user folder is reconfigured to support OpenID authentication.
 * An OpenID login portlet is added to the left column.
 * The standard login form is replaces with a form which supports both
   OpenID logins and standard username & password logins.
