FROM schemaspy/schemaspy:6.1.0

USER root

# Install git, openssh for CI
# Install pip (python2.7) to install aws-cli
RUN apk add --no-cache git openssh py-pip \
	&& pip install --upgrade pip \
	&& pip install --upgrade awscli
