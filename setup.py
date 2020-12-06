import setuptools
from flomo import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flomo",
    version=__version__,
    author="Benature Wang",
    author_email="wbenature@163.com",
    description="Flomo API (third party)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Benature/flomo",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'bs4'],
    # entry_points={
    #     'console_scripts': [
    #         'autolatex=autolatex:excel2table',
    #         'alt=autolatex:excel2table',
    #     ],
    # },
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires='>=3.7',
)

'''
pip uninstall flomo -y
rm -rf ./dist
rm -rf ./build
python setup.py sdist bdist_wheel
pip install -U dist/flomo-0.0.1-py3-none-any.whl
twine upload dist/*
'''
