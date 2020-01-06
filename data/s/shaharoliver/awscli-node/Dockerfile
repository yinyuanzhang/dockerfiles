FROM node:8.16.0

RUN apt-get update

RUN apt-get install python-dev python-pip -y

RUN easy_install --upgrade six

RUN pip install awscli

RUN apt-get install zip

CMD ["/bin/bash"]
