FROM alpine:3.6

RUN apk add --no-cache python3

RUN apk --update add --virtual build-dependencies python3-dev \
  && python3 -m ensurepip \
  && pip3 install click jira flask prometheus_client \
  && apk del build-dependencies

ADD main.py main.py

RUN chmod 555 main.py

EXPOSE 9060

ENTRYPOINT ["/main.py"]

CMD ["--help"]
