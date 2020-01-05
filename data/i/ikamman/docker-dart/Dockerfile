FROM ubuntu

RUN apt-get install -y apt-transport-https curl
RUN curl -s https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN curl -s https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list
RUN apt-get update
RUN apt-get install -y dart

# Clean apt
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set up PATH variable
ENV PATH $PATH:/usr/lib/dart/bin

RUN mkdir /app
WORKDIR /app
VOLUME /app

EXPOSE 8080

CMD ["dart", "--version"]