FROM alpine:3.9
# now using 3.9 to get a more recent version of node

# copied from atlassian/pipelines-awscli

ARG VERSION
ENV AWS_CLI_VERSION=$VERSION

RUN apk --update --no-cache add \
    python \
    py-pip \
    jq \
    bash \
    git \
    groff \
    less \
    mailcap \
    bash \
#     && pip install --no-cache-dir awscli==$AWS_CLI_VERSION \
    && pip install --no-cache-dir awscli \
    && apk del py-pip \
    && rm -rf /var/cache/apk/* /root/.cache/pip/*

# aditional ausvet functionality

#SETUP ausvet required packages
# install python3
RUN export LANG=en_AU.UTF-8 && \
    apk add curl python3 libffi bash
# setup pipenv
RUN python3 -m ensurepip && \
    pip3 --version && \
    pip3 install -U pipenv
# setup aws ecs-cli
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest && \
    chmod +x /usr/local/bin/ecs-cli
# setup nodejs
RUN apk add --update nodejs nodejs-npm yarn
# setup sentry
RUN npm install -g @sentry/cli --unsafe-perm

# FROM PARENT 
WORKDIR /root
VOLUME /root/.aws

# ENTRYPOINT [ "aws" ]
# CMD ["--version"]
ENTRYPOINT ["/bin/bash"]
# CMD ["/bin/bash"]
