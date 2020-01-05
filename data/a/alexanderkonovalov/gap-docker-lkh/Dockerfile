FROM gapsystem/gap-docker

MAINTAINER Alexander Konovalov <alexk@mcs.st-andrews.ac.uk>

RUN    cd /home/gap/inst/ \
    && wget -q http://akira.ruc.dk/~keld/research/LKH/LKH-2.0.9.tgz \
    && tar xvfz LKH-2.0.9.tgz \
    && cd LKH-2.0.9 \
    && make

ENV PATH /home/gap/inst/LKH-2.0.9:${PATH}

# Set up new user and home directory in environment.
# Note that WORKDIR will not expand environment variables in docker versions < 1.3.1.
# See docker issue 2637: https://github.com/docker/docker/issues/2637
USER gap
ENV HOME /home/gap
ENV GAP_HOME /home/gap/inst/gap-4.9.3
ENV PATH ${GAP_HOME}/bin:${PATH}

# Start at $HOME.
WORKDIR /home/gap

# Start from a BASH shell.
CMD ["bash"]
