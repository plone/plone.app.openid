from setuptools import setup, find_packages

version = '2.0.2'

setup(name='plone.app.openid',
      version=version,
      description="Plone OpenID authentication support",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='Plone OpenID authentication consumer',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.app.openid',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages = ['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
        'setuptools',
        'plone.openid',
        'plone.portlets',
        'plone.app.portlets',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'Products.CMFCore',
        'Products.PlonePAS>=2.0.10dev',
        'Products.PluggableAuthService',
        'Zope2',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
