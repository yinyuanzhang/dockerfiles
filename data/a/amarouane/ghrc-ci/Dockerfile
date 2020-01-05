FROM continuumio/miniconda3
LABEL maintainer="am0089@uah.edu" \
     author="Abdelhak Marouane"
RUN apt-get update && \
    apt-get install -y zip
RUN useradd -u 1000 -ms /bin/bash gitlabci 
#Install dependencies
RUN apt-get install -y libxml2-utils
RUN pip install pytest-cov
RUN pip install awscli
USER gitlabci 
ENV HOME=/home/gitlabci
WORKDIR $HOME
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash 

COPY requirements.sh $HOME/ 
RUN . $HOME/requirements.sh
