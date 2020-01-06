FROM debian:stretch

RUN apt-get update \
	&& apt-get install -y \
		build-essential \
		curl

WORKDIR /tmp
RUN curl "https://code.call-cc.org/releases/5.0.0/chicken-5.0.0.tar.gz" \
	| tar xz

WORKDIR /tmp/chicken-5.0.0
RUN make PLATFORM=linux \
	&& make PLATFORM=linux install \
	&& make PLATFORM=linux check

FROM debian:stretch

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		build-essential \
		git \
		ssh \
		tar \
		gzip \
		ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

COPY --from=0 /usr/local/bin /usr/local/bin
COPY --from=0 /usr/local/lib /usr/local/lib
COPY --from=0 /usr/local/include/chicken /usr/local/include/chicken
COPY --from=0 /usr/local/share/chicken /usr/local/share/chicken
