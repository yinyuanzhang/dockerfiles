FROM alpine
RUN apk update
RUN apk add bash
RUN apk add openssh
RUN apk add openjdk8
RUN apk add wget
RUN apk add git
RUN apk add unzip
RUN apk add apache-ant --update-cache \
	--repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
	--allow-untrusted
#Drop salesforce migration tool into the ant/lib so it can be used for deployment
ENV ANT_HOME /usr/share/java/apache-ant
ENV PATH $PATH:$ANT_HOME/bin
