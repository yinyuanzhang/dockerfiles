FROM openjdk:8-jdk-stretch

LABEL maintainer="dwe@ecadia.de"

ENV TZ Europe/Berlin
ENV ANT_HOME /usr/share/ant
ENV PATH "~/bin:${PATH}"

RUN apt update && \
	apt install -y ant gettext-base subversion zip unzip wget&& \
	mkdir ~/bin && \
	curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo && \
	chmod a+x ~/bin/repo
	
