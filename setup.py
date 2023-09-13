import os
import setuptools


setuptools.setup(
    name='server',
    version="0.1.dev0",
    author="Mustafa Ahmet PeSEN",
    author_email="mustafa.pesen@metu.edu.tr, ygt.psn@gmail.com",
    packages=setuptools.find_packages(),
    description='Deep learning for preventing tomato disease',
    long_description=open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'README.md')).read(),
    license='MIT',
    url='',
    install_requires=['numpy', 'scipy', 'matplotlib', 'pandas', 'moviepy', 'numba',
                      'pillow', 'six', 'easydict', 'pyyaml'],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence'],
)