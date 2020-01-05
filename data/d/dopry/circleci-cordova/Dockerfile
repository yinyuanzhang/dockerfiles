FROM circleci/android:api-24-node8-alpha
LABEL maintainer="https://spry-group.com"
RUN sudo apt-get update && sudo apt-get install -y \
    # gradle is required for cordova-android >= 6.4.0
    gradle \
    && sudo rm -rf /var/lib/apt/lists/*
RUN sudo npm install -g cordova@8.0.0