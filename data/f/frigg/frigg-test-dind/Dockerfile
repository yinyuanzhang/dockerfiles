FROM docker:1.8

# https://github.com/docker/docker/blob/master/project/PACKAGERS.md#runtime-dependencies
RUN apk add --update \
		btrfs-progs \
		e2fsprogs \
		iptables \
		xz \
		musl \
		bash \
		python \
		python3 \
		python-dev \
		py-pip \
		build-base \
		git \
	    && pip install -U virtualenv pip \
        && rm -rf /var/cache/apk/*

RUN apk add --update docker

# TODO aufs-tools

ENV DIND_COMMIT b8bed8832b77a478360ae946a69dab5e922b194e

RUN wget "https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O /usr/local/bin/dind \
	&& chmod +x /usr/local/bin/dind

COPY dockerd-entrypoint.sh /usr/local/bin/

VOLUME /var/lib/docker
EXPOSE 2375

ENTRYPOINT ["dockerd-entrypoint.sh"]
CMD []
