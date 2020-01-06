###   Start by creating a "builder"   ###
# We'll compile all needed packages in the builder, and then
# we'll just get only what we need for the actual APP

# Use an official Python runtime as a parent image
FROM python:3.7-slim as builder

## install the gcc compiler
#  (needed to install some of the python packages):
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    g++ \
    pkg-config \
    make \
    cmake \
    # also install git, needed to build dcm2niix:
    git-core \
  && apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y

## For now, install 'emacs', to be able to edit packages
#  in the builder, and 'curl'
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    emacs \
    curl \
  && apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y

# Install dcmstack from github (using git):
ENV DCMSTACK_VERSION=v0.7
RUN mkdir /tmp/dcmstack && \
    curl -sSL https://github.com/moloney/dcmstack/archive/${DCMSTACK_VERSION}.tar.gz \
        | tar -vxz -C /tmp/dcmstack --strip-components=1 && \
    cd /tmp/dcmstack && \
    easy_install ./ && \
    cd / && rm -rf /tmp/dcmstack

# Install dcm2niix from github:
# Install also pigz-- it makes dcm2niix compress NIfTI files faster
ENV DCM2NIIX_VERSION=v1.0.20190410
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y pigz && \
    apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && \
    \
    mkdir /tmp/dcm2niix && \
    curl -sSL https://github.com/rordenlab/dcm2niix/archive/${DCM2NIIX_VERSION}.tar.gz \
        | tar -vxz -C /tmp/dcm2niix --strip-components=1 && \
    cd /tmp/dcm2niix && \
    mkdir build && cd build && cmake -DBATCH_VERSION=ON .. && \
    make && make install && \
    cd / && rm -rf /tmp/dcm2niix

# Install heudiconv from github:
RUN cd /tmp && \
    git clone https://github.com/cbinyu/heudiconv.git && \
    cd heudiconv && \
    pip install . && \
    cd / && rm -rf /tmp/heudiconv
#COPY [".", "/tmp/heudiconv"]
#RUN cd /tmp/heudiconv && \
#    pip install . && \
#    cd / && rm -rf /tmp/heudiconv


# Get rid of some test folders in some of the Python packages:
# (They are not needed for our APP):
#RUN rm -fr /usr/local/lib/python3.7/site-packages/numpy
RUN rm -fr /usr/local/lib/python3.7/site-packages/nibabel/nicom/tests && \
    rm -fr /usr/local/lib/python3.7/site-packages/nibabel/tests       && \
    rm -fr /usr/local/lib/python3.7/site-packages/nibabel/gifti/tests

#############

###  Now, get a new machine with only the essentials  ###

FROM python:3.7-slim as Application

COPY --from=builder ./usr/local/lib/python3.7/ /usr/local/lib/python3.7/
COPY --from=builder ./usr/local/bin/           /usr/local/bin/
COPY --from=builder ./usr/bin/pigz             /usr/bin/

# Run app.py when the container launches:
#ADD . /app
ENTRYPOINT ["/usr/local/bin/heudiconv"]
