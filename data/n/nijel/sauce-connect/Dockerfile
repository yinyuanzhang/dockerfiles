FROM debian:buster-slim
MAINTAINER Michal Čihař <michal@cihar.com>
ENV VERSION 4.5.4
LABEL version=$VERSION

WORKDIR /app

RUN apt-get update -qqy \
 && apt-get install -qqy wget \
 && apt-get clean

RUN wget https://saucelabs.com/downloads/sc-$VERSION-linux.tar.gz -O - | tar -xz --strip 1

# Entrypoint
COPY start /app/bin/
RUN chmod a+rx /app/bin/start

EXPOSE 4445
EXPOSE 8032
USER 1000
ENTRYPOINT ["/app/bin/start"]
CMD ["auto"]
