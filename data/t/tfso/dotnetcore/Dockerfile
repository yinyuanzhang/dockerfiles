FROM microsoft/dotnet:2.1-aspnetcore-runtime
#RUN apk add --update openssh git bash && rm -rf /var/cache/apk/*
RUN apt-get -y update
RUN apt-get -y install w3m p7zip-full
RUN mkdir -p /start/src

WORKDIR /start

COPY startup.sh ./

# give all execution rights
RUN chmod 777 startup.sh

# copy private key
#RUN mkdir -p /root/.ssh/
#COPY ssh/ /root/.ssh/
#RUN chmod 700 /root/.ssh
#RUN chmod 600 /root/.ssh/*

WORKDIR /start/src

ENTRYPOINT ["bash","/start/startup.sh"]
