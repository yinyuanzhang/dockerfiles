FROM frolvlad/alpine-glibc

MAINTAINER Loic Gouarin "loic.gouarin@gmail.com"

# Configure environment
ENV CONDA_DIR=/opt/conda CONDA_VER=4.3.11
ENV PATH=$CONDA_DIR/bin:$PATH SHELL=/bin/bash LANG=C.UTF-8
ENV USER=precis

# Install useful packages 
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories &&\
    apk --update add \
    bash \
    curl \
    git \
    ca-certificates \
    tini@testing \
    libice \
    libsm \
    libstdc++ \
    freeglut &&\
    rm -rf /var/cache/apk/*

RUN curl https://repo.continuum.io/miniconda/Miniconda3-${CONDA_VER}-Linux-x86_64.sh  -o mconda.sh 

RUN /bin/bash mconda.sh -f -b -p $CONDA_DIR && \
    rm mconda.sh 

COPY environment.yml environment.yml
RUN conda env create -f environment.yml &&\
    rm -rf $CONDA_DIR/pkgs

ENV PATH=$CONDA_DIR/envs/$USER/bin:$PATH
ENV CONDA_ENV_PATH=$CONDA_DIR/envs/$USER
ENV CONDA_DEFAULT_ENV=$USER

RUN adduser -s /bin/bash -D $USER

WORKDIR /home/$USER
EXPOSE 1234
# Configure container startup
ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "lab", "--ip=*", "--port=1234" ,"--no-browser"]

# Setup home directory
RUN mkdir /home/$USER/.jupyter && \
    echo "cacert=/etc/ssl/certs/ca-certificates.crt" > /home/$USER/.curlrc

USER $USER

RUN mkdir -p /home/$USER/.config/matplotlib &&\
    echo "backend      : Agg" >> /home/$USER/.config/matplotlib/matplotlibrc

# Clone the shifman files into the docker container
RUN git clone https://github.com/ReScience-Archives/Shifman-2017.git shifman

