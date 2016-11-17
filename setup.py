from setuptools import setup, find_packages

setup(name='esgissue-client',
      version='0.1c',
      description='Local client to create, update, close and retrieve ESGF issues',
      author='Levavasseur Guillaume',
      author_email='glipsl@ipsl.jussieu.fr',

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: Unix',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering',
          'License :: OSI Approved :: MIT License',
      ],

      url='https://github.com/ES-DOC/esdoc-errata-client',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['requests>=2.9.1',
                        'jsonschema',
                        'functools32'
                        ],
      platforms=['Unix'],
      zip_safe=False,
      entry_points={'console_scripts': ['esgissue=esgissue.esgissue:run']},
      )
