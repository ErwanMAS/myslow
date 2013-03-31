from distutils.core import setup

setup(name='MySlow',
      version='0.0.1',
      description='Play with mysql slow log',
      author='Mathieu Lecarme',
      author_email='mlecarme@bearstech.com',
      url='https://github.com/bearstech/myslow',
      package_dir={'': 'lib'},
      packages=['myslow', 'myslow.output'],
      scripts=['scripts/myslow']
      )
