FROM kcyeu/python:latest
MAINTAINER Gordon Yeu <kcyeu@mikuru.tw>

ENV REQUIREMENTS_FILE /requirements.txt
ADD ${REQUIREMENTS_FILE} /

RUN apt update && \
	apt upgrade -y && \
	DEPS="gcc autoconf git" && \
	apt install -y ${DEPS} && \
	pip install python3-keyczar && \
	pip install -r ${REQUIREMENTS_FILE} && \
	apt remove -y ${DEPS} && \
	apt autoremove -y && \
	rm -f ${REQUIREMENTS_FILE}

WORKDIR /
