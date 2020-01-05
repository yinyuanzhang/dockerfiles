FROM alpine:3.9.4

RUN apk add --update --no-cache python3 jq git curl bash && \
    pip3 install --no-cache --upgrade pip && \
    pip3 install --no-cache awscli ansi2html

RUN adduser -D scriptuser
USER scriptuser

WORKDIR /home/scriptuser
RUN git clone https://github.com/toniblyx/prowler.git && mkdir /home/scriptuser/.aws
WORKDIR prowler
