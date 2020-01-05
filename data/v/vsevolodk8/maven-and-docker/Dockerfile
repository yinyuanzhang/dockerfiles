FROM docker:stable

RUN apk add --no-cache \
        bash \
        maven \
        openjdk8 \
        git

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["sh"]