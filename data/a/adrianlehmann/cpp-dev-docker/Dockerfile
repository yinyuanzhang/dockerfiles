FROM ubuntu:18.04
MAINTAINER Adrian Lehmann adrian.lehmann@student.kit.edu
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git openssh-client
RUN apt-get install -y gcc g++-8 clang cmake libboost-dev libboost-iostreams-dev libboost-program-options-dev libc++-dev
RUN apt-get install -y clang-format
RUN apt-get install -y default-jdk
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y python3.6
# Set the locale
RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV LC_LANG en_US.UTF-8
ENV PYTHONIOENCODING utf-8
ENV LC_CTYPE UTF-8
