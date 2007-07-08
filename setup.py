from setuptools import setup, find_packages

version = '1.0rc2'

setup(name='plone.app.openid',
      version=version,
      description="Plone OpenID authentication support",
      long_description="""\
""",
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/plone/plone.app.openid',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      download_url='http://code.google.com/p/plone/downloads/list',
      install_requires=[
        'plone.openid',
        'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
