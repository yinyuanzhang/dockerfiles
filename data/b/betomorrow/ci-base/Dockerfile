FROM docker:stable

RUN apk --no-cache --update-cache add \
        bash \
        curl \
        openssh-client \
        jq \
        git \
        moreutils \
        py-pip \
        python &&\
    pip install --upgrade \
      pip \
      yq

RUN ln -s /opt/bats/bin/bats /usr/sbin/bats
COPY bats-core-1.1.0 /opt/bats/

COPY bashbrew-amd64.1106d3b /usr/local/bin/bashbrew

COPY entrypoint.sh /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/bin/sh"]
