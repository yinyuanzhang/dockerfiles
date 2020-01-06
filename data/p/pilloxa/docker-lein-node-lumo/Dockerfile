FROM circleci/clojure:openjdk-8-lein-2.9.1-node
MAINTAINER Viktor Eriksson <viktor.eriksson2@gmail.com>
# Insall nvm and upgrade to latest node
ENV NODE_VERSION=12.13.0
ENV HOME="/home/circleci"
ENV NVM_DIR="$HOME/.nvm"
RUN mkdir $NVM_DIR
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
RUN echo ". $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default" | bash 
RUN sudo npm i npm@latest -g
RUN sudo npm install -g lumo-cljs@1.10.1 --unsafe-perm
ENV PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:${PATH}"
ENV PATH="/home/circleci/android-sdk/tools/bin:${PATH}"
ENV ANDROID_HOME="/home/circleci/android-sdk"

RUN mkdir -p /home/circleci/android-sdk && cd /home/circleci/android-sdk && \
wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip && \ 
unzip *tools*linux*.zip && \
rm *tools*linux*.zip


RUN yes | sdkmanager "build-tools;28.0.3"
RUN yes | sdkmanager "ndk-bundle"
RUN sudo apt-get install ninja-build

# Install clojure cli utilities
RUN curl -O https://download.clojure.org/install/linux-install-1.10.1.483.sh && chmod +x linux-install-1.10.1.483.sh && sudo ./linux-install-1.10.1.483.sh