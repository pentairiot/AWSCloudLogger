from setuptools import setup


with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name='AWSCloudLogger',
    version='0.0.2',
    author='PentairIoT',
    author_email='pentairiot@gmail.com',
    description='Lambda function and Library for writing and reading logs to and from SQS or CloudWatch',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pentairiot/AWSCloudLogger',
    install_requires=["boto3"],
    packages=["SQSLogger", "CloudwatchLogger"],
    package_dir={'': 'lib'},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
