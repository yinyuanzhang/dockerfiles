FROM alpine:3.7

ENV HEROKU_CLI_VERSION '7.5.4'

RUN addgroup -S ops && adduser -S -G ops ops 

RUN set -ex \
  && apk add --update --no-cache py-pip build-base python-dev libffi-dev openssl-dev \
	&& pip install ansible \
  && pip install cryptography \
  && pip install heroku3 \
	&& apk del build-base py-pip libffi-dev openssl-dev

ENV ANSIBLE_CONFIG /ops/etc/ansible/conf/ansible.cfg

RUN set -ex \
  && apk add --update --no-cache shadow zsh bash curl nodejs

# RUN curl https://cli-assets.heroku.com/install.sh | sh

RUN npm install -g yarn
RUN yarn global add heroku@$HEROKU_CLI_VERSION

RUN set -ex \
  && mkdir /app

COPY ./conf/docker-entrypoint.sh /bin/docker-entrypoint.sh

COPY ./conf/zshrc /home/ops/.zshrc

USER ops

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["zsh"]
