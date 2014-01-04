try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
    'msgpack-python',
]
setup(name='pynnrpc',
      version='1.0',
      py_modules=['nn'],
      install_requires=requirements,
      )
