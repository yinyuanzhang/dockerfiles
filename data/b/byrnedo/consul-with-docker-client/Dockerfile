FROM consul:latest

RUN apk --update add --no-cache docker

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["agent", "-dev", "-client", "0.0.0.0"]
