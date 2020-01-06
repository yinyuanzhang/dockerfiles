FROM hashicorp/packer:light

ENV AWSCLI_VER 1.16.33

RUN set -x \
    && apk add --update --no-cache ansible py-pip \
    && pip install --upgrade awscli==$AWSCLI_VER \
    && rm /var/cache/apk/*

WORKDIR /tmp

ENTRYPOINT ["/bin/bash", "-c"]
