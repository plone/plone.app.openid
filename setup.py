from setuptools import setup, find_packages

version = '2.1.1'

setup(
    name='plone.app.openid',
    version=version,
    description="Plone OpenID authentication support",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Plone OpenID authentication consumer',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/plone.app.openid',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        test=['plone.app.testing']
    ),
    install_requires=[
        'setuptools',
        'plone.openid',
        'plone.portlets',
        'plone.app.portlets',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'Products.CMFPlone',
        'Products.PlonePAS>=2.0.10dev',
        'Products.PluggableAuthService',
        'Zope2',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
