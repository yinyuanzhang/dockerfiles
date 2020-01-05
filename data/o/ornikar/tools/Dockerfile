FROM alpine:3.11

# Maintainers.
LABEL maintainer="Julien BREUX <julien.breux@ornikar.com>"

ENV USR_BIN=/usr/bin
ENV PATH=$PATH:/root/.local/bin
ENV HELM_HOME=/var/lib/helm

# Install some packages.
RUN apk add --update --no-cache \
        curl=7.67.0-r0 \
        git=2.24.1-r0 \
        openssh-client=8.1_p1-r0 \
        docker-cli=19.03.5-r0 \
        bash=5.0.11-r1 \
        zip=3.0-r7 \
        python \
        python-dev \
        py-pip \
        build-base \
        # Task installation
        && mkdir /lib64 \
        && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
        && curl -LJ "https://github.com/go-task/task/releases/download/v2.8.0/task_linux_amd64.tar.gz" -s -o task.tar.gz \
        && mkdir task \
        && tar -xvzf task.tar.gz -C task \
        && mv task/task "${USR_BIN}" \
        && rm -Rf task task.tar.gz \
        # Codefresh installation
        && curl -LJ "https://github.com/codefresh-io/cli/releases/download/v0.40.0/codefresh-v0.40.0-alpine-x64.tar.gz" -s -o codefresh.tar.gz \
        && mkdir codefresh \
        && tar -xvzf codefresh.tar.gz -C codefresh \
        && mv codefresh/codefresh "${USR_BIN}" \
        && rm -Rf codefresh codefresh.tar.gz \
        # Helm installation
        && curl -LJ "https://get.helm.sh/helm-v3.0.2-linux-amd64.tar.gz" -s -o helm.tar.gz \
        && mkdir helm \
        && tar -xvzf helm.tar.gz -C helm \
        && mv helm/linux-amd64/helm "${USR_BIN}/helm" \
        && rm -Rf helm helm.tar.gz \
        # Helm plugins
        && helm plugin install https://github.com/chartmuseum/helm-push \
        # AWS Client
        && pip install awscli --upgrade --user --no-warn-script-location \
        # Check
        && task --version \
        && codefresh version \
        && helm version \
        && helm plugin list \
        && aws --version \
        # Clean
        && rm -rf /var/cache/apk/*
