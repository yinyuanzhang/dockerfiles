FROM bitnami/minideb:stretch
LABEL maintainer "Chris Wells <chris@cevanwells.com>"

RUN install_packages build-essential curl 

WORKDIR /app
RUN mkdir dvdid
RUN curl -sSL "http://dvdid.cjkey.org.uk/dvdid-0.1.1.tar.gz" -o "dvdid.tar.gz" \
	&& tar -zxvf dvdid.tar.gz -C /app/dvdid --strip 1 \
	&& rm -f "dvdid.tar.gz"

WORKDIR /app/dvdid
RUN ./configure --prefix=/usr \
	&& make \
	&& make install

WORKDIR /app