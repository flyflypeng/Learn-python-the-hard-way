try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config ={
    'description': 'My Test Project',
    'author': 'woshijpf',
    'author_email': 'woshijpfgg@gmai.com',
    'url': 'http://woshijpf.github.io',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['TestSetup'],
    'scripts': [],
    'name': 'Test Setup Project'
}

setup(**config)