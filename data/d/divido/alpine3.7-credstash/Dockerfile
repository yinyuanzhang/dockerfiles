FROM alpine:3.7

RUN  apk add --no-cache --virtual .dd-build-deps alpine-sdk python3-dev openssl-dev libffi-dev && \
	 apk add --no-cache python3 openssl ca-certificates && \
	 pip3 install credstash && \
	 apk del .dd-build-deps