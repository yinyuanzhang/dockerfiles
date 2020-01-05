FROM lsiobase/python:3.10

ARG BUILD_DATE
ARG VERSION
ARG NUT_RELEASE
LABEL build_version="version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL mantainer="fldc"

# set python to use utf-8 rather than ascii.
ENV PYTHONIOENCODING="UTF-8"

RUN \
 echo "**** install app ****" && \
 mkdir -p \
	/app/nut && \
 if [ -z ${NUT_RELEASE+x} ]; then \
 	NUT_RELEASE=$(curl -sX GET "https://api.github.com/repos/blawar/nut/commits/master" \
        | awk '/sha/{print $4;exit}' FS='[""]'); \
 fi && \
 curl -o \
	/tmp/nut.tar.gz -L \
	"https://github.com/blawar/nut/archive/${NUT_RELEASE}.tar.gz" && \
 tar xf /tmp/nut.tar.gz -C \
	/app/nut --strip-components=1 && \
 echo "**** install dependencies ****" && \
 apk add --no-cache --upgrade \
 	python3 \
	py3-openssl \
	py3-requests \
	py3-unidecode \
	py3-pillow \
	py3-beautifulsoup4 \
 	py3-urllib3 \
	py3-flask \
	py3-cffi \
	py3-qt5 && \
 cd /app/nut && \
 pip3 --no-cache-dir install \
	colorama \
	tqdm \
	image \
	image \
	pyusb && \
 echo "**** Cleanup ****" && \
 rm -Rf /tmp/*

# add local files
COPY root/ /
COPY nut.conf /app/nut/conf
COPY start.sh /bin

# ports and volumes
EXPOSE 9000 
WORKDIR /app/nut
VOLUME /config

