FROM circleci/node:8.10

RUN sudo apt-get update && sudo apt-get install python python-pip python-dev build-essential && \
    curl -s -o- -L https://yarnpkg.com/install.sh | bash && sudo rm -rf /usr/local/bin/yarn && \
    sudo ln -s /home/circleci/.yarn/bin/yarn /usr/local/bin/yarn && \
    sudo pip install awscli --upgrade
