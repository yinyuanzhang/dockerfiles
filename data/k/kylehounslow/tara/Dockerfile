FROM nvidia/cuda:9.0-devel-ubuntu16.04
ENV CUDNN_VERSION 7.0.5.15
RUN apt-get update && apt-get install -y --no-install-recommends \
            libcudnn7=$CUDNN_VERSION-1+cuda9.0 \
            libcudnn7-dev=$CUDNN_VERSION-1+cuda9.0 && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install -y software-properties-common # for add-apt-repository
RUN apt-get install -y curl bash-completion
RUN apt-get install -y git vim
RUN apt-get install -y imagemagick
RUN apt-get install -y build-essential python3-pip python3-venv
# add ffmpeg support and codec for video read/write
RUN apt-get update
RUN apt-get install -y ffmpeg
# This line accepts the Microsoft End User License Agreement allowing use of
#   the MS True Type core fonts
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN apt-get install -y ubuntu-restricted-extras
# update pip
RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel
# install jupyter and widgets
RUN python3 -m pip install jupyter

# install numpy before tensorflow (in requirements.txt)
RUN python3 -m pip install numpy
# install tensorflow deps
RUN apt-get install -y graphviz libgraphviz-dev
#install requirements.txt
COPY requirements-gpu.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

# install jupyter-tensorboard
RUN python3 -m pip install jupyter-tensorboard
RUN /usr/local/bin/jupyter-tensorboard enable

#some env vars to fix bug with Click lib in python3
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# uninstall some libs to trim down image size
RUN apt-get remove -y g++ gcc ssh make build-essential
RUN apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

# add symlink to python3
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN apt-get install -y python3-tk

# create user with same UID as host (typically uid=1000, gid=100)
ENV TARA_USER=tara_docker
RUN useradd -r -u 1000 -g 100 $TARA_USER

# copy all required files to project directory
ENV TARA_DIR="/home/tara"
RUN mkdir "$TARA_DIR"
WORKDIR $TARA_DIR
ADD cfg/ $TARA_DIR/cfg/
ADD gcloud $TARA_DIR/gcloud/
ADD tara $TARA_DIR/tara/
ADD *.py $TARA_DIR/
ADD matlab/ $TARA_DIR/matlab/
ADD scripts/ $TARA_DIR/scripts/
RUN chmod 777 /home -R

# tara env setup
ENV PYTHONPATH="$PYTHONPATH:$TARA_DIR"

# install gcloud sdk
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-xenial main" > /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update
RUN apt-get install -y google-cloud-sdk
# re-add symlink to python3, it gets reset during installation of above packages
RUN ln -sf /usr/bin/python3 /usr/bin/python
USER $TARA_USER
ENV GOOGLE_APPLICATION_CREDENTIALS="$TARA_DIR/gcloud/service_accounts/docker-container-key.json"
RUN gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
RUN gcloud config set project tarantula-3d-project
USER root
ENV TARA_BIN=/usr/local/bin/tara
RUN echo '#!/bin/bash\npython $TARA_DIR/cli.py "$@"' > $TARA_BIN && chmod +x $TARA_BIN
# add a welcome message
ADD cli/welcome.txt $TARA_dir/cli/
RUN chmod 777 /home -R

USER $TARA_USER
WORKDIR /home/work
ENTRYPOINT cat $TARA_dir/cli/welcome.txt && /bin/bash
ENV TARA_USER=$TARA_USER
