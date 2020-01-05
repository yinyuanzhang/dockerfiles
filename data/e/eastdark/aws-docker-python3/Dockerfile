# Copyright 2017-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License"). You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#    http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file.
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied.
# See the License for the specific language governing permissions and limitations under the License.
#

FROM dannyzhong/python3node7

RUN apt-get update

ENV DOCKER_BUCKET="get.docker.com" \
    DOCKER_VERSION="1.12.1" \
    DOCKER_SHA256="05ceec7fd937e1416e5dce12b0b6e1c655907d349d52574319a1e875077ccb79" \
    DIND_COMMIT="3b5fac462d21ca164b3778647420016315289034"

COPY dockerd-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh  # https://github.com/moby/moby/issues/27182

RUN set -x \
    && curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
    && echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
    && tar -xzvf docker.tgz \
    && mv docker/* /usr/local/bin/ \
    && rmdir docker \
    && rm docker.tgz \
    && docker -v \
# From the docker dind 1.11
    && apt-get update && apt-get install -y --no-install-recommends \
       e2fsprogs iptables xfsprogs xz-utils \
# set up subuid/subgid so that "--userns-remap=default" works out-of-the-box
    && addgroup dockremap \
    && useradd -g dockremap dockremap \
    && echo 'dockremap:165536:65536' >> /etc/subuid \
    && echo 'dockremap:165536:65536' >> /etc/subgid \
    && wget "https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O /usr/local/bin/dind \
    && chmod +x /usr/local/bin/dind \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

##########################################################################
#  Customize the build environment for our own stack
##########################################################################

# Install node8. node7 can't be installed on ubuntu 17.10 (https://github.com/nodesource/distributions/issues/543)
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install --yes nodejs
RUN pip3 install --upgrade pip setuptools
RUN pip3 install --upgrade --user awscli

RUN apt-get install --yes jq
# upgrade jq to 1.5. http://stackoverflow.com/questions/36462955/upgrading-jq-to-1-5-on-ubuntu
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 \
     && chmod +x jq-linux64 \
     && mv jq-linux64 $(which jq)


VOLUME /var/lib/docker

ENTRYPOINT ["dockerd-entrypoint.sh"]
