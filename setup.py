from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Our first Package',
      author='Andrii Truba',
      author_email='truba.a@icloud.com',
      license='MIT',
      packages=find_namespace_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
      )