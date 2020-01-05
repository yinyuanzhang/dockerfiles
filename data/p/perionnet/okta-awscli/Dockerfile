FROM ubuntu:18.04
ARG okta-release-tag=2.0.0

RUN apt-get update 
RUN apt-get install openjdk-11-jre -y
RUN apt-get install curl -y

# Install python and pip
RUN apt-get install python3 python3-distutils -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
# Install aw-cli
RUN pip3 install awscli --upgrade

# Install okta-aws-cli-assume-role
# Note: we currently use installation from forked repo as build 2.0.2 is broken
RUN curl https://raw.githubusercontent.com/sharon-vendrov/okta-aws-cli-assume-role/master/bin/install.sh -o install.sh
RUN chmod +x install.sh
RUN PREFIX=~/.okta && ./install.sh -i

RUN echo '#OktaAWSCLI\n\
if [[ -f "$HOME/.okta/bash_functions" ]]; then\n\
    . "$HOME/.okta/bash_functions"\n\
fi\n\
if [[ -d "$HOME/.okta/bin" && ":$PATH:" != *":$HOME/.okta/bin:"* ]]; then\n\
    PATH="$HOME/.okta/bin:$PATH"\n\
fi\n'\
>> ~/.bash_profile

# Workaround from executing 'source ~/.bash_profile' on container startup
COPY okta-aws /usr/local/bin

RUN chmod +x /usr/local/bin/okta-aws
ENTRYPOINT [ "/usr/local/bin/okta-aws", "default", "sts", "get-caller-identity" ]