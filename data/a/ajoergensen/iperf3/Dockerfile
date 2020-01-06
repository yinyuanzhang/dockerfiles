FROM alpine:3.9

MAINTAINER ajoergensen

RUN \
	apk --no-cache upgrade && \
	apk --no-cache add iperf3

EXPOSE 5201

ENTRYPOINT ["iperf3"]
