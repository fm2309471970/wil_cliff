# setup.py
from setuptools import setup, find_packages

setup(
    name='wil_cliff',
    version='0.1',
    packages=find_packages(),
    description='A package to perform Wilcoxon test and Cliff\'s Delta analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='fanmeng',
    author_email='2309471970@qq.com',
    url='https://github.com/fm2309471970/wil_cliff',
    install_requires=[
        'scipy',
        'cliffs-delta'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)