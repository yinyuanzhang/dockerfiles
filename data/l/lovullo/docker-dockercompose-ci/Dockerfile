FROM docker:dind

RUN apk add --update python py-pip curl \
    && pip install docker-compose \
    && rm -rf /var/cache/apk/*

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["sh"]
