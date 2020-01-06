FROM fedora:latest

RUN dnf upgrade -y && \
    dnf install -y python-pip \
                git \
                graphviz \
                findutils \
                gfortran && \
                pip install ford
