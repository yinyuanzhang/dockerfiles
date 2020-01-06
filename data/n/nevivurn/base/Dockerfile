FROM alpine:3.10

# Runit & minor quality-of-life
RUN apk add --no-cache \
	bash \
	runit \
	tzdata \
	vim

COPY . /docker

ENV TZ=Etc/UTC
WORKDIR /docker
VOLUME /docker/log
CMD ["/docker/init"]
