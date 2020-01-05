FROM fpco/stack-build:lts-12.26

SHELL ["/bin/bash", "-c"]

ENV BASH_ENV $HOME/.bash_profile

RUN sudo apt-get update -y && \
    sudo apt-get remove -y nodejs && \
    sudo apt-get install -y librocksdb-dev && \
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash && \
    echo 'export NVM_DIR=$HOME/.nvm' >> $BASH_ENV && \
    echo 'source $NVM_DIR/nvm.sh' >> $BASH_ENV

RUN nvm install node && \
    npm install -g yarn
