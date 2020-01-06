# Copyright (C) 2019 Glamping Hub (https://glampinghub.com)
# All rights reserved

FROM alpine

LABEL \
    version="1.0"

RUN apk add --no-cache npm \
    && npm install --production -g elasticdump \
    && rm -rf /var/cache/apk/* /tmp/*

ENTRYPOINT ["elasticdump"]
