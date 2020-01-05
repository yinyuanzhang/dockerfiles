# Copyright 2018 SwiftStack, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM python:2.7

LABEL maintainer="Trey Duskin <trey@swiftstack.com>"

WORKDIR /ssapi

#build/install code
COPY . ./
RUN pip install -r docker-requirements.txt
RUN python setup.py install

#set up activate command
RUN chmod +x ./activate.sh && ln -s `pwd`/activate.sh /bin/activate

#set up volumes and workdir
RUN mkdir /workdir
VOLUME /workdir
WORKDIR /workdir

