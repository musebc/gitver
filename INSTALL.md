# Installation instructions

`gitver` can be installed either via `pip` or by checking out the repository, the place where all the development happens.

By using the latter you'll be able to choose between *stable* or *development* releases, while on [PyPI](https://pypi.python.org/pypi) only stable versions are uploaded to PyPI.


## Requirements

#### Environment

You'll need these packages to be installed.

- Python 2.7, 3.6, 3.7, 3.8, 3.9
- the `git` tool

## Install via repository

You are going to need to install `setuptools` and `pip`, so use your package manager or any other means for this.


#### Clone the project

When done, you can proceed to clone the project from [github](https://github.com/musebc/gitver):

    git clone git@github.com:musebc/gitver.git


#### Install project requirements

Now we should satisfy the project's requirements. This project uses Flit to build the project. You will need to install Flit for your system following the instructions here: [Flit Installation](https://flit.readthedocs.io/en/latest/index.html#install) 

    $ cd gitver
    $ python3 -m venv env
    $ source ./env/bin/activate
    $ pip install flit
    $ flit install --deps develop --symlink

At this point, you should be ready to run `gitver` directly from the repository:

    $ bin/gitver version
    This is gitver n/a
    Full build ID is n/a
    ...

You probably noticed there is no version information there, this will be done automatically when installing, but for now let's generate it manually:

    $ bin/gitver update version
    Processing template "version" for /tmp/gitver.git/gitver/_version.py...
    Done, 207 bytes written.

    $ bin/gitver version
    This is gitver v0.3.0-RC1.69+8f975ed
    Full build ID is 8f975ed5c1195038f71db36ccc6c1c5b2b8cacd3
    ...