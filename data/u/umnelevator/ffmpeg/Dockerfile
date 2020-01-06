FROM        ubuntu:18.04 as build

WORKDIR     /tmp/workdir

RUN     apt-get -yqq update && \
        apt-get --no-install-recommends -yqq install software-properties-common && \
        rm -rf /var/lib/apt/lists/*

RUN     add-apt-repository ppa:jonathonf/ffmpeg-4 && \
        apt-get -yqq update && \
        apt-get --no-install-recommends -yqq install gpac ffmpeg="7:4.1.3-0york1~18.04" && \
        rm -rf /var/lib/apt/lists/*

MAINTAINER  Colin McFadden <mcfa0086@umn.edu>

WORKDIR     /scratch/
