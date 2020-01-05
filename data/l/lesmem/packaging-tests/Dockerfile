FROM ubuntu:bionic
RUN apt-get update && apt-get install -y curl lsb-release python3-pip openjdk-8-jdk gcc ruby-dev openssh-client rsync sudo pandoc nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
	echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
	apt-get update && \
	apt-get install -y yarn
RUN pip3 install sh jinja2 psutil
RUN curl -O "https://releases.hashicorp.com/vagrant/2.2.5/vagrant_2.2.5_x86_64.deb" && \
	dpkg -i "vagrant_2.2.5_x86_64.deb" && \
	rm "vagrant_2.2.5_x86_64.deb" && \
	mkdir "/etc/vagrant/" && \
	VAGRANT_HOME="/etc/vagrant/" vagrant plugin install vagrant-google vagrant-host-shell && \
	curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
	echo "deb https://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
	apt-get update && \
	apt-get install -y google-cloud-sdk
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
	echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list && \
	apt-get update && \
	apt-get install -y docker-ce
VOLUME /keys/google.json /keys/ssh.key
ENV GOOGLE_SSH_KEY_LOCATION="/keys/ssh.key" GOOGLE_JSON_KEY_LOCATION="/keys/google.json"
ADD entrypoint /usr/bin/
ENTRYPOINT ["entrypoint"]
