FROM jenkins/jenkins:lts

# Change user to root do download packages
USER root

# Install required python packages
RUN apt-get update && apt-get install -y \
	python3.5-dev \
	python3-pip \
	python-setuptools \
	openssl

# Install python modules
RUN pip3 install paramiko paramiko-expect

# Delete all the apt list files to keep clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Return to default jenkins user
USER jenkins