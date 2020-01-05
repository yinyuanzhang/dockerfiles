FROM node:10-alpine

ENV YARN_VERSION 1.16.0

RUN apk upgrade \
    && apk add --update --no-cache curl bash git openssh ca-certificates groff less python3 \
    # install yarn
    && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
    && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
    && ln -snf /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
    && ln -snf /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
    && rm yarn-v$YARN_VERSION.tar.gz \
    # install pip3
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools \
    && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \
    && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi \
    # install aws-cli
    && pip3 install --upgrade pip setuptools \
    && pip3 --no-cache-dir install awscli --upgrade \
    # remove temp packages
    && apk del curl \
    # clean caches
    && npm cache clean --force \
    && yarn cache clean \
    && rm -rf /var/cache/apk/* \
    && rm -rf /root/.cache \
    && echo "------------ DONE -------------" \
    # verify
    && yarn --version \
    && aws --version

CMD ["/bin/bash"]