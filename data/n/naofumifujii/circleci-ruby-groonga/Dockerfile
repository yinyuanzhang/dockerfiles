FROM circleci/ruby:2.6.4-stretch-node-browsers

RUN sudo sh -c "echo 'deb [signed-by=/usr/share/keyrings/groonga-archive-keyring.gpg] https://packages.groonga.org/debian/ stretch main' >> /etc/apt/sources.list.d/groonga.list" && \
    sudo sh -c "echo 'deb-src [signed-by=/usr/share/keyrings/groonga-archive-keyring.gpg] https://packages.groonga.org/debian/ stretch main' >> /etc/apt/sources.list.d/groonga.list" && \
    sudo sh -c "echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >> /etc/apt/sources.list.d/pgdg.list" && \
    sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - && \
    sudo apt-get install -y postgresql-client && \
    sudo apt-get install -y apt-transport-https && \
    sudo apt-get update -qq && \
    sudo apt-get install -y --allow-unauthenticated groonga-keyring && \
    sudo apt-get install -y --force-yes groonga groonga-tokenizer-mecab libgroonga-dev
