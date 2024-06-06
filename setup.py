from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        # 'some_package>=1.0.0',
    ],
    author='Susmitha',
    author_email='susmitha0978@gmail.com',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/susmitha-106/my_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
      entry_points={
        'console_scripts': [
            'my_package=my_package.__main__:main',
        ],
    },
)
