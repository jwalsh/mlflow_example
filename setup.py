from setuptools import setup

setup(name='mlflow_example',
      version='0.1.0',
      packages=['mlflow_example'],
      entry_points={
          'console_scripts': [
              'mlflow_example = mlflow_example.__main__:main'
          ]
      },
      )
