"""
"""
from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(
    name='BAVA',
    version='0.1',
    url='https://github.com/BrainArteryNetwork/BAVA',
    license='MIT',
    author='BrainArteryNetwork',
    author_email='kennyz@uw.edu',
    description='Brain Artery Visualization & Analysis Tool',
    packages=PACKAGES,
    package_data={'bava': ['api/*', 'streamlit/*', 'visualization3d/*', 'tests/*']}

)

if __name__ == '__main__':
    setup(**opts)