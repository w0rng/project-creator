from setuptools import setup, find_packages
import projectcreator
from os.path import join, dirname


setup(
    name='projectcreator',
    version=projectcreator.__version__,
    author=projectcreator.__author__,
    description='Package for create projects',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    url='https://github.com/w0rng/project-creator',
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['create_project = projectcreator:main']
        }
)
