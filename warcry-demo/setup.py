import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'marshmallow==2.0.0b4',
    'pyramid==1.5.7',
    'pyramid-debugtoolbar==2.4',
    'pyramid-tm==0.12',
    'SQLAlchemy==1.0.6',
    'transaction==1.4.4',
    'zope.sqlalchemy==0.7.6',
    'waitress==0.8.9',
    ]

setup(name='warcry-example',
      version='0.0',
      description='warcry-example',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Nico Karsas',
      author_email='nico.karsas@alchimea.com',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='warcryexample',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = warcryexample:main
      [console_scripts]
      initialize_warcry-example_db = warcryexample.scripts.initializedb:main
      """,
      )
