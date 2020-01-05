FROM debian:latest

RUN  apt-get update && \
     apt-get install -y curl && \
     curl -sL https://deb.nodesource.com/setup | bash - && \
     apt-get install -y nodejs \
     	     	     build-essential \
			git \
			emacs23-nox    
COPY pre-commit /usr/share/git-core/templates/hooks/

