FROM node:8.15.0
RUN npm install -g @c8y/cli
RUN mkdir /home/c8y
RUN apt-get update
RUN apt-get install -y vim
WORKDIR /home/c8y
EXPOSE 9000