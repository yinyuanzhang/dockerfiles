FROM bitriseio/docker-android:latest

# ------------------------------------------------------
# --- Install required tools

RUN apt-get update -qq

# ------------------------------------------------------
# --- Cordova CLI

RUN yarn global add cordova
RUN cordova -v

# ------------------------------------------------------
# --- Install Ant

RUN apt-get install -y ant
RUN ant -version


# ------------------------------------------------------
# --- Install Quasar
RUN yarn global add @quasar/cli
RUN quasar -v

# ------------------------------------------------------
# --- Cleanup and rev num

# Cleaning
RUN apt-get clean

ENV BITRISE_DOCKER_REV_NUMBER_ANDROID_CORDOVA 2016_01_24_1
CMD bitrise -version
