FROM alpine

ARG VIRTUAL_HOST

COPY Gemfile /Gemfile
COPY startup.sh /startup.sh

RUN echo -e "install: --no-document\nupdate: --no-document" > /etc/gemrc \
    && apk update \
    && apk upgrade \
    && apk add --no-cache --virtual .build-deps \
        g++ \
        git \
        make \
    && apk add --no-cache \
        ruby \
        ruby-dev \
        ruby-json \
    && gem install bundler \
    && bundle install -j4 \
    && apk del .build-deps \
    && mkdir /sqs

EXPOSE 9494

CMD ["sh", "startup.sh"]
