#!/usr/bin/env python
import demo
from setuptools import setup, find_packages

install_requires = [

]

setup(
    name='plynx-demo',
    version='0.0.1',
    description='ML platform',
    long_description='Interactive, Scalable, Shareable and Reproducible ML experiments',
    url='https://plynx.com',
    author='Ivan Khomyakov',
    author_email='ivan@plynx.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Console',
        'Environment :: Web Environment',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: POSIX',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',

        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords='data science, machine learning, pipeline, workflow, experiments',
    packages=find_packages(),
    install_requires=install_requires,
    package_data={},
    project_urls={
        'Demo': 'https://plynx.com',
        'Source': 'https://github.com/plynx-team/plynx',
    },
    # plynx.graph.base_nodes.collection uses reference to __file__
    zip_safe=False,
)
