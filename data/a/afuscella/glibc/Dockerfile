FROM alpine:3.7
MAINTAINER Arthur Silva <fuscellaarthur@gmail.com>

# Upgrade Alpine and install additional packages
RUN echo http://nl.alpinelinux.org/alpine/x86_64/community >> /etc/apk/repositories
RUN apk upgrade --update && \
    apk add --no-cache $ALL_DEPS && \
    apk upgrade &&\    
	apk add -f gnupg --no-cache &&\
	apk add ca-certificates --no-cache &&\
	apk add bash --no-cache

# Install GLIBC 2.28 [jdk/jre compatible]
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk
RUN apk add glibc-2.28-r0.apk &&\
	rm glibc-2.28-r0.apk