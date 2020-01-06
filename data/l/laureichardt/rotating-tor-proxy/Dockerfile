# HAProxy base image
FROM haproxy:1.8-alpine

# add tor and privoxy
RUN apk add --no-cache tor privoxy 

# add s6 overlay
RUN apk add --no-cache curl \
	&& curl -L -s https://github.com/just-containers/s6-overlay/releases/download/v1.22.1.0/s6-overlay-amd64.tar.gz \
	| tar xvzf - -C / \
	&& apk del --no-cache curl

# copy services to run on start up
COPY rootfs /

# expose ports
EXPOSE 2090 5566 8118 9001 9002

# init
ENTRYPOINT [ "/init" ]