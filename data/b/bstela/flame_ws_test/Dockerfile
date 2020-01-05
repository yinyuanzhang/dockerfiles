FROM continuumio/miniconda3

LABEL base.image="continuumio/miniconda3"
LABEL software="flame"
LABEL software.version=" v0.1-alpha"
LABEL description="Python scripts to build and manage QSAR models. Predictive modeling within the eTRANSAFE (http://etransafe.eu) project."
LABEL website="https://github.com/phi-grib/flame"

MAINTAINER Biel Stela <biel.stela@upf.edu>

ENV USER=phi-grib
ENV REPO=flame
ENV BRANCH=padel_request

ENV WSBRANCH=docker
ENV WSREPO=flame_ws

WORKDIR /opt

RUN apt-get update &&\
    apt-get install -y libxrender-dev libgl1-mesa-dev &&\
    apt-get clean -y &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# cloning flame repo. First clone to get access to the environment.yml
# then pull with commit changes awareness to rebuild from the next layer
# and avoid instaling al the libraries every build.
ADD https://api.github.com/repos/$USER/$REPO/git/refs/heads/$BRANCH version.json
RUN git clone -b $BRANCH --single-branch https://github.com/$USER/$REPO.git &&\
    cd flame && \
    conda env create -f environment.yml

# hand activate conda environment    
ENV PATH /opt/conda/envs/flame/bin:$PATH

ADD https://api.github.com/repos/$USER/$WSREPO/git/refs/heads/master version.json
RUN cd flame/ &&\
    pip install . &&\
    cd /opt &&\
    git clone -b $WSBRANCH --single-branch https://github.com/$USER/$WSREPO.git
# hack to don't use cache if repo haves new commits
# ADD https://api.github.com/repos/$USER/$REPO/git/refs/heads/$BRANCH version.json
# RUN cd flame && \
#     git pull https://github.com/$USER/$REPO.git


WORKDIR /opt/flame_ws/flame_ws

RUN cp -R /opt/flame/flame/models/ /opt/ &&\
    flame -c config -p /opt/models/

COPY BSEP_model /opt/models/BSEP_model

EXPOSE 8081

ENTRYPOINT [ "python", "flame-ws.py" ]
