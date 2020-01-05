FROM node:10.15.3-alpine@sha256:b85a3b0ef76f5543b3f467e8a25694e72594d2c2bfcf140fa584d4f40ace4130

RUN apk add --no-cache ca-certificates
RUN apk add --no-cache --virtual native-deps curl \
    && curl https://github.com/gmr/env-aws-params/releases/download/0.2.0/env-aws-params_0.2.0_alpine-linux_amd64.zip -s -O -J -L \
    && echo "d8f23fa813c84e1e64b3023cb3b179cd  env-aws-params_0.2.0_alpine-linux_amd64.zip" > env-aws-params.md5 \
    && md5sum -c env-aws-params.md5 \
    && rm env-aws-params.md5 \
    && unzip -d /usr/local/bin/ env-aws-params_0.2.0_alpine-linux_amd64.zip \
    && rm env-aws-params_0.2.0_alpine-linux_amd64.zip \
    && apk del native-deps
