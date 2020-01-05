# Copyright 2015 The Kubernetes Authors. All rights reserved.
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

FROM node:0.12.10-wheezy
ADD . kube-ui
EXPOSE 8090

RUN cd /kube-ui/master && \
	npm install -g bower && \
	npm install -g http-server && \
	npm run build

CMD /bin/bash -c 'cd /kube-ui/app; http-server -a localhost -p 8090'
