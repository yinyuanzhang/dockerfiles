FROM node:alpine
RUN apk add --no-cache git
RUN apk add --no-cache openssh
RUN apk add --no-cache python
RUN apk add --no-cache py2-crypto
RUN mkdir /data  
RUN mkdir /config
RUN mkdir /u01
RUN git clone https://github.com/ddurdle/Python-GoogleDrive-VideoStream.git /data/app && rm -rf /data/app/releases
WORKDIR /data/app
COPY ./startgdv.sh . 
ENV DB=/config/gdrive.db
ENV STARTMODE=DEFAULT
ENTRYPOINT ["/data/app/startgdv.sh"]
EXPOSE 9988
