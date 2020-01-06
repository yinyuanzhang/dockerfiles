FROM gliderlabs/alpine:3.4
MAINTAINER Peter McConnell <peter.mcconnell@rehabstudio.com>

# add the registry
RUN echo "http://dl-6.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
	apk update && \
	apk add docker bash make && \
	rm -rf /var/cache/apk/*

CMD ["bash"]
