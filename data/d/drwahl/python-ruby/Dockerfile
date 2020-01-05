FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python python-pip
RUN apt-get -y install ruby ruby-dev
RUN apt-get -y install git
RUN pip install -U pre-commit
RUN gem install rubocop --no-doc --no-ri
