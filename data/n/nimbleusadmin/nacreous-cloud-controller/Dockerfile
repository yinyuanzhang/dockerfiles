FROM ubuntu:14.04
MAINTAINER Nimbleus, LLC
RUN apt-get update
RUN apt-get install -y -q software-properties-common python-software-properties
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y unzip
RUN apt-get install -y wget
RUN apt-get install -y -q oracle-java8-installer
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /var/cache/oracle-jdk8-installer
RUN curl -k -L -o nacreous-cloud-controller-1.0.0-RC9.zip -unimbleus:8540ad9b559fb5ae28775a4c0831751c0ef004bf 'https://dl.bintray.com/nimbleus/nacreous/nacreous-cloud-controller-1.0.0-RC9.zip'
RUN mkdir /app
RUN mv nacreous-cloud-controller-1.0.0-RC9.zip /app
WORKDIR /app
RUN unzip nacreous-cloud-controller-1.0.0-RC9.zip
WORKDIR /app/nacreous-cloud-controller-1.0.0-RC9/bin
RUN chmod +x /app/nacreous-cloud-controller-1.0.0-RC9/bin/nacreous-cloud-controller
EXPOSE 80
ENTRYPOINT ["/app/nacreous-cloud-controller-1.0.0-RC9/bin/nacreous-cloud-controller"]
