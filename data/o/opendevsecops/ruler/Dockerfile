FROM circleci/golang:latest

WORKDIR /

RUN true \
    && go get -u github.com/sensepost/ruler

ENTRYPOINT ["ruler"]
