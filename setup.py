from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '1.0.3'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='skt-war-result',
    version=__version__,
    entry_points={"console_scripts": ["skt-war-result = sktwar.main:main"]},
    description='Lists war results for Japanese servers in Lineage Mobile game.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yumenoshima/skt-war-result',
    download_url='https://github.com/yumenoshima/skt-war-result/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='yumenoshima',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='skt.tofuya@gmail.com'
)
