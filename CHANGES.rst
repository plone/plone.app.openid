Changelog
=========


2.1.1 (2016-05-24)
------------------

Fixes:

- Code quality package cleanup.  [maurits]


2.1.0 (2015-03-12)
------------------

- Read ``use_email_as_login`` settings from the registry instead of portal
  properties (see https://github.com/plone/Products.CMFPlone/issues/216). This
  means we also need to depend on Products.CMFPlone instead of
  Products.CMFCore.
  [jcerjak]


2.0.3 (2015-02-11)
------------------

- Ported tests to plone.app.testing
  [tomgross]


2.0.2 (2012-01-26)
------------------

- Use fixed spelling of method name hasOpenIDExtractor from PlonePAS.
  We depend on Products.PlonePAS 2.0.10dev or higher for this.
  Fixes http://dev.plone.org/ticket/11040
  [maurits]

- Add MANIFEST.in.
  [WouterVH]


2.0.1 - 2010-07-18
------------------

- Update license to GPL version 2 only.
  [hannosch]


2.0 - 2010-07-01
----------------

- 'login' is a noun; 'log in' is a verb. Fixes #10025.
  [davisagli]


2.0b3 - 2010-02-17
------------------

- Updated login-related templates to the recent markup conventions.
  References http://dev.plone.org/plone/ticket/9981.
  [spliter]

- Updated templates to disable the columns with 'disable_MANAGER_NAME' pattern.
  [spliter]


2.0b2 - 2009-12-27
------------------

- Clarified package metadata.
  [hannosch]


2.0b1 - 2009-12-01
------------------

- Make html structure of openid login section similar to plone login
  section so that we can use same css.
  [smcmahon]

- Point to users to @@register instead of @@join_form.
  [esteele]


2.0a1 - 2009-11-17
------------------

- Correctly implement the 'available' property of the portlet renderer so
  that a column with only an openid portlet doesn't show up when logged in.
  [davisagli]

- Make sure the GenericSetup profile shows up on the Plone site add form.
  [davisagli]

- Added a metadata.xml to the GenericSetup profile.
  [davisagli]

- Register the ploneopenid-various GenericSetup import step using ZCML.
  [davisagli]

- Replaced the css_slot with the style_slot, as it is deprecated.
  [maurits]

- Made compatible with Plone 4.0.  Show different labels on login form
  when site_properties/use_email_as_login is switched on (Plone 4.0).
  Should still work in earlier Plones.
  Refs http://dev.plone.org/plone/ticket/9214
  [maurits]

- Made the addLoginPortlet function a bit more forgiving, when portlets aren't
  available.
  [hannosch]

- Added the z3c.autoinclude entry point so this package is automatically loaded
  on Plone 3.3 and above.
  [hannosch]

- Avoid a test dependency on quick installer.
  [hannosch]

- Use our own PloneMessageFactory and remove the dependency on CMFPlone.
  [hannosch]

- Specified package dependencies.
  [hannosch]


1.1.1 - 2010-09-19
------------------

- Removed msgids in portlets.xml. There is no support for
  msgids in the import of portlets.xml implementation.
  This allows to extract translatable strings with i18ndude.
  [vincentfretin]


1.1 - 2008-08-19
----------------

- Added missing customized version of login_failed.cpt which was causing an
  error on a failed standard login when OpenID support is installed.  This closes
  http://dev.plone.org/plone/ticket/7268
  [davisagli]

- Now including plone.app.portlets in the zcml. Fixes zope instance
  startup error under certain circumstances.
  [maurits]


1.0.3 - 2008-04-21
------------------

- Added missing i18n markup to portlets.xml.
  [hannosch]

- Fixed erroneous (duplicate) translation ID. This fixes
  http://dev.plone.org/plone/ticket/7764
  [limi]



1.0.2 - 2008-05-07
------------------

- Correct the title of the portlet type to read 'OpenID Login' instead of
  just 'Login'.
  [wichert]


1.0.1 - 2007-08-17
------------------

- Remove use of javascript in login portlet
  [ree]


1.0 - 2007-08-15
----------------

- First stable release.
  [wichert]
