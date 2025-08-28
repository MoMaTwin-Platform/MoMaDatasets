from setuptools import setup, find_packages

setup(
    name='MoMaDatasets',  
    version='0.1.0', 
    description='MoMaDatasets', 
    packages=find_packages(),  
    python_requires='>=3.6', 
    install_requires=[  
        'numpy',
        'imagecodecs-numcodecs',
    ],
)