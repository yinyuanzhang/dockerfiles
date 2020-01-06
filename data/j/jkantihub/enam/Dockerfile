# Docker file to create enam container
FROM centos:7
MAINTAINER Kanti Jadia

# Repository info up to date
RUN yum -y update && yum install -y wget epel sudo tar

# Add the mystack user that will run the browser
RUN groupadd -g 500 mystack && useradd -u 500 -g 500 mystack && \
    echo "mystack ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/mystack && \
    chmod 0440 /etc/sudoers.d/mystack  && \
    export uid=500 gid=500 

#Install node
RUN wget -qO- https://rpm.nodesource.com/setup | bash - && \
    yum install -y nodejs && \
    npm install npm && \
    npm install -g n && \
    n 0.12 && \
    npm install angular && \
    npm install express
