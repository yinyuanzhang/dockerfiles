FROM nvidia/cuda:10.1-devel-ubuntu18.04

# update repository information
RUN apt-get update --fix-missing

# install gcc/build tools and gsl
RUN apt-get install -y --no-install-recommends \
    build-essential libgsl23 libgslcblas0 libgsl-dev libgsl-dbg

# install some packages for development (optional)
RUN apt-get install -y --no-install-recommends \
    vim git

# cleanup install cache
RUN rm -rf /var/lib/apt/lists/*

# establish user, home directory
RUN useradd -rm -d /home/developer -s /bin/bash \
    -g root -G root -u 1000 developer
USER developer
ENV HOME /home/developer

CMD [ "/bin/bash" ]
