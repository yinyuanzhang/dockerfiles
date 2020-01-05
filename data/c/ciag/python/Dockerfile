FROM fedora:latest
RUN dnf update -y && dnf upgrade -y
RUN dnf groupinstall "Development Tools" -y
RUN dnf install which gcc-c++ python37 python3-devel -y
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN python -m pip install -U pip pipenv
RUN python -m pip install -U setuptools twine

