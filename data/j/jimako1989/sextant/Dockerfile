FROM jupyter/scipy-notebook
MAINTAINER jimako1989

## login as root
USER root

### Upgrade repository
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential && \
    apt-get install -y software-properties-common
# RUN apt-key adv --keyserver keys.gnupg.net --recv-keys C0B21F32
RUN apt-get update && apt-get install -y --no-install-recommends \
		bzip2 \
		unzip \
		xz-utils \
	&& rm -rf /var/lib/apt/lists/*

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

### Install OpenJDK
RUN apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get install -y oracle-java8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

### Install bazel
RUN wget https://github.com/bazelbuild/bazel/releases/download/0.18.1/bazel-0.18.1-installer-linux-x86_64.sh \
    && chmod +x ./bazel-0.18.1-installer-linux-x86_64.sh \
    && ./bazel-0.18.1-installer-linux-x86_64.sh


### Check version
RUN bazel version


### Install python modules
COPY requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt
