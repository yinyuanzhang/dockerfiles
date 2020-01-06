# Copyright 2014 TWO SIGMA OPEN SOURCE, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# to build: sudo docker build -t ubuntu/beaker .
# to run:   sudo docker run -p 8800:8800 -t ubuntu/beaker
# results hosted at: https://registry.hub.docker.com/u/beakernotebook/beaker/

FROM beakernotebook/beaker-base:latest

MAINTAINER Beaker Feedback <beaker-feedback@twosigma.com>

###################
#      Build      #
###################

ADD . /home/beaker/src

ENV HOME /home/beaker

RUN chown -R beaker:beaker /home/beaker

RUN su -m beaker -c "cd /home/beaker/src  && gradle build"

###################
#      Setup      #
###################

RUN su -m beaker -c "julia --eval 'Pkg.add(\"IJulia\")'" && \
    su -m beaker -c "julia --eval 'Pkg.add(\"Requests\")'" && \
    su -m beaker -c "julia --eval 'Pkg.add(\"Gadfly\")'"
RUN su -m beaker -c "julia --eval 'Pkg.rm(\"IJulia\")'" && \
    su -m beaker -c "julia --eval 'Pkg.add(\"IJulia\")'"

RUN cp -r /home/beaker/.local/share/jupyter/kernels/julia-0.4 /usr/local/share/jupyter/kernels/

RUN mkdir -p /home/beaker/.beaker/v1/config && \
    echo '{"pref-format" : "1", "languages" : {"Python3" : {"path": "/home/beaker/py3k/bin"}}}' > /home/beaker/.beaker/v1/config/beaker.pref.json

RUN chown -R beaker:beaker /home/beaker/.beaker

###################
#       Run       #
###################

EXPOSE 8800
WORKDIR /home/beaker/src
CMD su -m beaker -c "export PATH=$PATH:/usr/sbin && /home/beaker/src/core/beaker.command --public-server --no-password"
