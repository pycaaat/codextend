from setuptools import setup, find_packages

setup(
    name='codextend',
    version='1.0.0',
    packages=find_packages(),
    description='A Python module The encoding and the encoding format can be converted.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="caaat",
    author_email='caaatstar@qq.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='code extension utility',
    python_requires='>=3.6',
    include_package_data=True,
)