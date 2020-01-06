FROM node:8
#RUN apt-get install -yy git perl
WORKDIR /usr/src/app
COPY . .
RUN npm install 
RUN npm install -g
RUN mkdir -pv /data
WORKDIR /data
ENTRYPOINT [ "/usr/local/bin/kcm" ]
