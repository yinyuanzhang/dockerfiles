FROM ruby:2.3.1

RUN (curl -sL https://deb.nodesource.com/setup_4.x | bash) && \
    apt-get update && \
    apt-get install -y nodejs git && \
    apt-get clean
RUN npm install -g bower

ADD start_container /usr/bin/start_container
RUN chmod +x /usr/bin/start_container
CMD start_container
