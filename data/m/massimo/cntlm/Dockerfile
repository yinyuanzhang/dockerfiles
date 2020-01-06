# explicitly use Debian for maximum cross-architecture compatibility
FROM debian:stretch-slim as cntlm-builder

LABEL maintainer="Massimo Ronca <massimo@mikamai.com>"

ENV http_proxy $HTTP_PROXY
ENV https_proxy $HTTP_PROXY

RUN apt-get update && apt-get install -y --no-install-recommends \
		make \
		libc-dev \
		musl-dev \
		musl-tools \
		patch \
		tar \
		gzip \
		wget \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/

ARG CNTLM_VERSION=0.92.3
ARG DOWNLOAD_URL=http://netcologne.dl.sourceforge.net/project/cntlm/cntlm
RUN wget -q ${DOWNLOAD_URL}/cntlm%20${CNTLM_VERSION}/cntlm-${CNTLM_VERSION}.tar.gz
RUN tar zxf cntlm-${CNTLM_VERSION}.tar.gz

WORKDIR cntlm-${CNTLM_VERSION}

ADD patches/Makefile.patch Makefile.patch
ADD patches/main.c.patch main.c.patch
RUN patch --dry-run -N --silent < Makefile.patch; [ $? -eq 0 ] && patch < Makefile.patch || true
RUN patch --dry-run -N --silent < main.c.patch; [ $? -eq 0 ] && patch < main.c.patch || true

RUN . ./configure
RUN make
RUN strip cntlm
RUN cp cntlm /

FROM scratch as cntlm

COPY --from=cntlm-builder /cntlm /

CMD [ "/cntlm", "-h"]