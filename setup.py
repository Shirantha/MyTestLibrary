#  Test RFW library

from setuptools import setup
from os.path import join, dirname, exists

execfile(join(dirname(__file__), 'MyLibrary', 'version.py'))

'''
def package_env(file_name, strict=False):
    file_path = join(dirname(__file__), file_name)
    if exists(file_path) or strict:
        return open(file_path).read()
    else:
        return ''
'''

setup(
    name='robotframework-MyLibrary',
    version=VERSION,
    author='SW',
    author_email='sw@xxmail.com',
    url='ToDo',
    license='Apache License 2.0',
    description='Test library using Robot Framework',
	long_description=open('README.txt').read(),
    #long_description=package_env('README.rst'),
    #package_dir={'': 'src'},
    #packages=['Pydblibrary', 'Pydblibrary.keywords'],
    #test_suite='test',
    install_requires=['robotframework>=2.7'],
    #platforms='any',
    #zip_safe=False
)
