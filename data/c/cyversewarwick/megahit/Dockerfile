FROM debian:latest

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install wget python zlib1g-dev build-essential

RUN wget https://github.com/voutcn/megahit/releases/download/v1.0.6/megahit_v1.0.6_LINUX_CPUONLY_x86_64-bin.tar.gz
RUN tar -xzf megahit_v1.0.6_LINUX_CPUONLY_x86_64-bin.tar.gz && rm megahit_v1.0.6_LINUX_CPUONLY_x86_64-bin.tar.gz
RUN mv megahit_v1.0.6_LINUX_CPUONLY_x86_64-bin megahit

RUN mkdir /scripts
COPY scripts /scripts

ENTRYPOINT ["bash", "/scripts/megahit_tarwrapper.sh"]