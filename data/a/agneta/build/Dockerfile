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

FROM docker:17-dind

ENV NPM_CONFIG_LOGLEVEL info

RUN apk -v --update add \
    nodejs \
    nodejs-npm \
    ca-certificates \
    iptables \
    ip6tables \
    python \
    py-pip \
    groff \
    less \
    curl \
    mailcap \
    && \
    pip install --upgrade awscli s3cmd python-magic docker-compose && \
    #----------------------
    docker-compose version && \
    #----------------------
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*

RUN npm install @agneta/cli@0.14.15 -g --no-shrinkwrap --unsafe-perm=true --allow-root
