FROM ubuntu

# Referring to https://gist.github.com/haelmy/6443125
RUN apt-get update
RUN apt-get install -y python-software-properties python g++ make
RUN add-apt-repository ppa:chris-lea/node.js
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y nodejs
RUN npm install -g tty.js

EXPOSE 3000
CMD ["tty.js", "--port", "3000"]
