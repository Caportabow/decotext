from setuptools import setup

setup(
    name='decotext',
    version='1.0',
    description='Generate unicode decorative text easy and fast.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Daniil Maistrenko',
    author_email='caportabow@gmail.com',
    license='MIT',
    packages=['decotext'],
    url= 'https://github.com/Caportabow/decotext',
    python_requires='>=3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='decorative unicode text generator',
)
