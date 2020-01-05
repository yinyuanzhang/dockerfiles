FROM alpine:latest

RUN apk add --no-cache bash gawk sed grep bc coreutils jq python py-pip && pip install --upgrade awscli

CMD ["/bin/bash"]
