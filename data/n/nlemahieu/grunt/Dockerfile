FROM ubuntu:14.04

RUN apt-get update && \
apt-get -y upgrade && \
apt-get install -y nodejs npm && \
npm install -g grunt-cli && \
npm install grunt-contrib-jshint --save-dev && \
npm install grunt-contrib-uglify --save-dev && \
npm install grunt-contrib-clean --save-dev && \
npm install grunt-contrib-concat --save-dev && \
npm install grunt-contrib-cssmin --save-dev && \
npm install grunt-contrib-less --save-dev && \
npm install --save-dev grunt-shell && \
npm install grunt-contrib-coffee --save-dev && \
npm install grunt-bower-task --save-dev && \
ln -s /usr/bin/nodejs /usr/bin/node

# Replace 1000 / 1000 by your user id and group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer