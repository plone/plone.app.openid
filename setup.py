from setuptools import setup, find_packages

version = '2.0a1'

setup(name='plone.app.openid',
      version=version,
      description="Plone OpenID authentication support",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone OpenID authentication consumer',
      author='Wichert Akkerman, Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/plone/plone.app.openid',
      license='GPL',
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
        'Products.PlonePAS',
        'Zope2',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
