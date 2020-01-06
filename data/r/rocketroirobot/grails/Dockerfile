FROM openjdk:8-jdk-slim

ENV GRAILS_VERSION 2.5.0
ENV GRAILS_HOME /usr/lib/jvm/grails
ENV PATH $GRAILS_HOME/bin:$PATH

ENV PATH="~/.local/bin:${PATH}"

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjfx \
    wget \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/lib/jvm

RUN wget https://github.com/grails/grails-core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip && \
    unzip grails-$GRAILS_VERSION.zip && \
    rm -rf grails-$GRAILS_VERSION.zip && \
    ln -s grails-$GRAILS_VERSION grails

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["grails"]
CMD ["run-app"]