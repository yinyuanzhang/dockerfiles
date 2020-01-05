FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv nuget gcc-8

RUN pip3 install conan
RUN pip3 install conan-package-tools
RUN pip3 install setuptools
RUN pip3 install virtualenv twine

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
