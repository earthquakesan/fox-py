from distutils.core import setup

setup(
    name='foxpy',
    version='1.0.0',
    author='Ivan Ermilov',
    author_email='earthquakesan@gmail.com',
    packages=['foxpy'],
    scripts=[],
    url='http://pypi.python.org/pypi/foxpy/',
    license='LICENSE.txt',
    description='Python bindings for FOX - Federated Knowledge Extraction Framework (python3)',
    long_description=open('README.txt').read(),
    install_requires=[
        'requests'
    ],
)

