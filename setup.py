from distutils.core import setup

setup(name='MySlow',
      version='0.0.2',
      description='Play with mysql slow log',
      author='Mathieu Lecarme',
      author_email='mlecarme@bearstech.com',
      url='https://github.com/bearstech/myslow',
      package_dir={'': 'src'},
      packages=['myslow', 'myslow.output'],
      scripts=['scripts/myslow']
      )
