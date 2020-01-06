FROM golang:1.9.4-alpine3.6

ENV DOCKER_CHANNEL edge
ENV DOCKER_VERSION 18.02.0-ce
ENV DOCKER_HOST='tcp://docker:2375'

ENV GITLAB_RUNNER_VERSION v10.7.0

COPY checksums.sha256 /tmp/
COPY entrypoint /

RUN addgroup -S gitlab-runner -g 1000 \
    && adduser -D -u 1000 -S -h /home/gitlab-runner -G gitlab-runner gitlab-runner \
    # Install packages
    && apk add --no-cache --update \
    bash \
    make \
    ca-certificates \
    git \
    openssl \
    tzdata \
    wget \
    btrfs-progs \
    e2fsprogs \
    e2fsprogs-extra \
    iptables \
    xfsprogs \
    xz \
    curl \
    # Install golang dep package manager
    && go get -u github.com/golang/dep/cmd/dep \
    # Install gitlab runner
    && wget  https://gitlab-runner-downloads.s3.amazonaws.com/$GITLAB_RUNNER_VERSION/binaries/gitlab-runner-linux-amd64 -O /usr/bin/gitlab-runner \
    && chmod +x /usr/bin/gitlab-runner \
    && ln -s /usr/bin/gitlab-runner /usr/bin/gitlab-ci-multi-runner \
    && gitlab-runner --version \
    && mkdir -p /etc/gitlab-runner/certs \
    && chmod -R 700 /etc/gitlab-runner \
    # Install docker-machine
    && wget  https://github.com/docker/machine/releases/download/v0.14.0/docker-machine-Linux-x86_64 -O /usr/bin/docker-machine \
    && chmod +x /usr/bin/docker-machine \
    && docker-machine --version \
    # Install dumb-init
    && wget  https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 -O /usr/bin/dumb-init \
    && chmod +x /usr/bin/dumb-init \
    && dumb-init --version \
    && sha256sum -c -w /tmp/checksums.sha256 \
    # Install docker
    && set -ex; \
    # why we use "curl" instead of "wget":
    # + wget -O docker.tgz https://download.docker.com/linux/static/stable/x86_64/docker-17.03.1-ce.tgz
    # Connecting to download.docker.com (54.230.87.253:443)
    # wget: error getting response: Connection reset by peer
        apk add --no-cache --virtual .fetch-deps \
            curl \
            tar \
        ; \
        \
    # this "case" statement is generated via "update.sh"
        apkArch="$(apk --print-arch)"; \
        case "$apkArch" in \
            x86_64) dockerArch='x86_64' ;; \
            armhf) dockerArch='armel' ;; \
            aarch64) dockerArch='aarch64' ;; \
            ppc64le) dockerArch='ppc64le' ;; \
            s390x) dockerArch='s390x' ;; \
            *) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\
        esac; \
        \
        if ! curl -fL -o docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz"; then \
            echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from '${DOCKER_CHANNEL}' for '${dockerArch}'"; \
            exit 1; \
        fi; \
        \
        tar --extract \
            --file docker.tgz \
            --strip-components 1 \
            --directory /usr/local/bin/ \
        ; \
        rm docker.tgz; \
        \
        apk del .fetch-deps; \
        \
        dockerd -v; \
        docker -v; \
        chmod +x /entrypoint

VOLUME ["/etc/gitlab-runner", "/home/gitlab-runner", "/var/lib/docker"]

ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]