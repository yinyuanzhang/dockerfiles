
FROM maven:3-jdk-10

RUN apt-get update -y && \
    apt-get install -y python python-pip apt-transport-https ca-certificates curl gnupg2 software-properties-common jq&& \
	curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
	add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" && \
	apt-get update && \
	apt-get -y install docker-ce && \
    pip install awscli --ignore-installed six && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*