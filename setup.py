from setuptools import setup
from setuptools import find_packages

setup(name='music_player',
      version='1.0',
      description='Music Player, Parses playlists from web and suggests playlists based on availability, reccomends more songs',
      author='Sahil Agarwal',
      author_email='sahil.agarwal94@gmail.com',
      keywords='music player playlists web suggests playlists reccomendation system',
      # url='',
      license='MIT',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Music Player and Reccomendation System',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ],

      packages=find_packages(),
      )
