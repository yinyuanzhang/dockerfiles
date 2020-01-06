# Copyright (c) 2018 Vente-Privée
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM vpgrp/debian:jessie

ENV DEBIAN_FRONTEND="noninteractive" \
    GEMS="/usr/local/rvm/gems/ruby-2.5.5" \
    RUBIES="/usr/local/rvm/rubies/ruby-2.5.5" \
    TZ="Europe/Amsterdam"

RUN apt-get update  -qq && \
    apt-get upgrade -qq -y && \
    apt-get install -qq -y \
      lsb-release \
      sudo \
      systemd \
      systemd-sysv && \
    apt-clean

RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import - && \
    curl -sSL https://rvm.io/pkuczynski.asc | gpg --import - && \
    curl -sSL https://get.rvm.io | bash -s stable

RUN bash -l -c 'rvm install 2.5.5' && \
    bash -l -c 'rvm --default use 2.5.5' && \
    bash -l -c 'gem install --no-document puppet --version 4.10.12' && \
    bash -l -c 'gem install --no-document --quiet serverspec rake net-ssh \
      busser busser-serverspec'

RUN ln -s ${RUBIES}/bin/gem  /usr/bin/gem && \
    ln -s ${RUBIES}/bin/ruby /usr/bin/ruby && \
    ln -s ${GEMS}/bin/puppet /usr/bin/puppet

ENV PATH="${RUBIES}/bin:${GEMS}/bin:${PATH}" \
    GEM_PATH="${GEMS}:${GEM_PATH}"
# EOF
