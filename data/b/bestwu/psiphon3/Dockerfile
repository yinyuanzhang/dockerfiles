FROM alpine:3.6
LABEL maintainer='Peter Wu <piterwu@outlook.com>'

RUN apk add --no-cache python2 wget py2-pexpect libcrypto1.0 zlib libc6-compat && \
	rm -fr /var/cache/apk/*

ADD pyclient /pyclient
EXPOSE 1080
WORKDIR /pyclient
CMD python psi_client.py