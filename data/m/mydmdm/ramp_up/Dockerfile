# based on https://github.com/TagineerDai/cu90-deep-learning-image
# building the base build of PAI (pai.build.base:hadoop2.7.2-cuda90-cudnn7-devel-ubuntu16.04)

FROM ufoym/deepo:all-jupyter-py36-cu90

LABEL maintainer='Yuqing Yang <justin.yqyang@gmail.com>'

# Essentials: developer tools, build tools, OpenBLAS
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils git curl vim unzip openssh-client wget \
    build-essential cmake \
    libopenblas-dev

#
# Python essential packages
#
# For convenience, alias (but don't sym-link) python & pip to python3 & pip3 as recommended in:
# http://askubuntu.com/questions/351318/changing-symlink-python-to-python3-causes-problems
RUN pip3 --no-cache-dir install \
    hdfs

#
# Jupyter Notebook
#
# Allow access from outside the container, and skip trying to open a browser.
# NOTE: disable authentication token for convenience. DON'T DO THIS ON A PUBLIC SERVER.
RUN pip3 --no-cache-dir install jupyter && \
    mkdir /root/.jupyter && \
    echo "c.NotebookApp.ip = '*'" \
         "\nc.NotebookApp.open_browser = False" \
         "\nc.NotebookApp.token = ''" \
         > /root/.jupyter/jupyter_notebook_config.py

RUN pip3 --no-cache-dir install jupyterlab


CMD ["/bin/bash"]


