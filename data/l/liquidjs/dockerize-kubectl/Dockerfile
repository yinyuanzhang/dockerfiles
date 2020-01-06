FROM docker:latest AS builder

WORKDIR /deps

RUN wget -O kubectl "https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/kubectl" \
    && chmod a+x kubectl

RUN wget -O dockerize.tar.gz "https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz" \
    && tar -xf dockerize.tar.gz \
    && chmod a+x dockerize

RUN wget -O jq "https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64" \
    && chmod a+x jq

RUN wget -O aws-iam-authenticator "https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator"\
    && chmod a+x aws-iam-authenticator


FROM docker:latest
RUN apk add py3-pip && pip3 install awscli
COPY --from=builder /deps/kubectl /deps/dockerize /deps/jq /deps/aws-iam-authenticator /usr/sbin/
