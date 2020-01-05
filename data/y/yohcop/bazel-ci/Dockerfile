# Installs bazel, node and python-yaml, which is needed by one build step.
# - python-yaml shoud be removed soon.
# - nodejs should also be removed, it's needed because some package post install
#   script calls node directly.
#
# Also installs google-cloud-sdk for continuous deployment.
# Note that authentication with the gcloud sdk should be handled during
# the coninuous integration/deployment scripts.

FROM openjdk:8

RUN apt-get update

###############################################################################
## Bazel

RUN apt-get install -y pkg-config zip g++ zlib1g-dev unzip python
RUN export BAZEL_VERSION=0.21.0 \
  && wget https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh \
  && chmod +x bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh \
  && ./bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh \
  && rm -rf bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh

###############################################################################
## Node
# This is needed for whatever reason, otherwise yarn install fails. I think
# a bad package (uglifyjs-webpack-plugin) may be calling "env node" binary
# directly...

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

###############################################################################
## Other packages I need
# patch is needed by bazel rules_go to "fix" some BUILD files or something.
RUN apt-get install -y python-yaml chromium patch

###############################################################################
## Cleanup after going to user ci.

RUN rm -rf /var/lib/apt/lists/*

###############################################################################
# Everything after that is executed as the 'ci' user.

RUN useradd -ms /bin/bash ci
USER ci
WORKDIR /home/ci

## Google Cloud

# NOTE: version is here and below since the export doesn't survive multiple
# RUN commands, and I wanted to keep the "expensive" wget separated from the
# rest of the commands.
RUN export GCLOUD_SDK_VERSION=222.0.0 \
  && wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${GCLOUD_SDK_VERSION}-linux-x86_64.tar.gz

RUN export GCLOUD_SDK_VERSION=222.0.0 \
  && export CLOUDSDK_CORE_DISABLE_PROMPTS=1 \
  && tar xf google-cloud-sdk-${GCLOUD_SDK_VERSION}-linux-x86_64.tar.gz --directory ${HOME} \
  && ${HOME}/google-cloud-sdk/install.sh \
  && export PATH=${PATH}:${HOME}/google-cloud-sdk/bin \
  && gcloud components install app-engine-go \
  && rm -rf google-cloud-sdk-${GCLOUD_SDK_VERSION}-linux-x86_64.tar.gz

## Chromedriver

RUN wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip -d ${HOME}/chromedriver \
  && export PATH=${PATH}:${HOME}/chromedriver \
  && rm -rf chromedriver_linux64.zip

## Add Google Could and Chromedriver to the path.

ENV PATH=${PATH}:/home/ci/google-cloud-sdk/bin:/home/ci/chromedriver
