FROM python:3.6-stretch

RUN apt update\ 
	&& apt-get install -y maven openjdk-8-jdk openjdk-8-jre python3-pip python3-dev apt-transport-https ca-certificates curl gnupg2 software-properties-common\
	&& update-alternatives --config java\
	&& curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -\
	&& add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"\
	&& apt-get update\
	&& apt-get install -y docker-ce docker-ce-cli containerd.io
