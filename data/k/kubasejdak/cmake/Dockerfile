FROM ubuntu:19.10
LABEL maintainer="Kuba Sejdak"

# Settings.
ARG CMAKE_VERSION=3.15.5
ENV CONAN_USER_HOME=/root

RUN apt-get update

# Install Python 3 and pip.
RUN apt-get install -y python3 python3-pip

# Install conan.
RUN pip3 install conan
RUN conan profile new default
RUN conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
RUN conan remote add conan-community https://api.bintray.com/conan/conan-community/conan

# Download CMake.
RUN apt-get install -y wget
RUN wget https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz
RUN mkdir -p /opt/cmake/${CMAKE_VERSION}
RUN tar -xf cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz -C /opt/cmake/${CMAKE_VERSION} --strip-components=1
RUN rm cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz
ENV PATH=/opt/cmake/${CMAKE_VERSION}/bin:${PATH}

# Install Doxygen and graphviz.
RUN apt-get install -y doxygen graphviz

# Install git and rsync.
RUN apt-get install software-properties-common -y
RUN apt-add-repository ppa:git-core/ppa -y
RUN apt-get install git rsync -y
