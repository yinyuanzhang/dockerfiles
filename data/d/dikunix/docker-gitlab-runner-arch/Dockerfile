FROM base/archlinux:latest

MAINTAINER Oleks <oleks@oleks.info>

RUN useradd -m docker

USER docker

WORKDIR /home/docker/

ENV PATH=/home/docker/.local/bin:$PATH

CMD ["/bin/bash"]
