FROM codeship/google-cloud-deployment
MAINTAINER Geoffroy Lesage "geoffroy@starchup.com"

RUN apt-get update
RUN apt-get install curl software-properties-common -y
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install nodejs git -y

CMD ["/bin/sh"]
