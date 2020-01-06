FROM        ubuntu:16.04

RUN         apt-get update && apt-get install curl -y && \
            curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
            apt-get install -y nodejs && \
            npm install -g --unsafe-perm @angular/cli