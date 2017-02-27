from setuptools import setup

setup(
    name='STEM-Greenhouse',
    version='1.0a1',
    packages=['STEM-Greenhouse'],
    author='Lukas Vann Struth',
    author_email='lvannstruth@gmail.com',
    license='MIT',
    classifiers=[
        'Developement Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License'
        'Programming Language :: Python 3.5'
    ],
    keywords='experimental school project arduino',
    install_requires=[
        'flask',
        'pyserial',
        'pygal',
    ],
)
