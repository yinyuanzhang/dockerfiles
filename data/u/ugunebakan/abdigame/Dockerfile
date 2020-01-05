FROM ubuntu
MAINTAINER Umut G
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y curl
# RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN curl https://install.meteor.com/ | sh
ADD . /opt/abdigame/app
WORKDIR /opt/abdigame/app/programs/server
# RUN npm install
WORKDIR /opt/abdigame/app
RUN ls -lart /opt/abdigame
ENV PORT 80
ENV ROOT_URL http://82.196.10.39
ENV MONGO_URL mongodb://mongo_instance:27017/abdigame
EXPOSE 80
# Start the app
CMD node ./main.js



# RUN meteor --port 82.196.10.39:3000


