# Copyright 2016 The Kubernetes Authors All rights reserved.
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

FROM nvidia/cuda:10.0-base
USER root
WORKDIR /data

# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
#        cuda-command-line-tools-9-0 \
#        cuda-cublas-9-0 \
#        cuda-cufft-9-0 \
#        cuda-curand-9-0 \
#        cuda-cusolver-9-0 \
#        cuda-cusparse-9-0 \
        curl \
#        libcudnn7=7.2.1.38-1+cuda9.0 \
#        libnccl2=2.2.13-1+cuda9.0 \
#        libfreetype6-dev \
#        libhdf5-serial-dev \
#        libpng12-dev \
#        libzmq3-dev \
#        pkg-config \
        python \
        python-dev \
#        rsync \
#        software-properties-common \
#        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py
RUN pip install celery gputil requests psutil

ADD celery_conf.py /data/celery_conf.py
#ADD run_tasks.py /data/run_tasks.py
ADD run.sh /usr/local/bin/run.sh

ENV C_FORCE_ROOT 1

CMD ["/bin/bash", "/usr/local/bin/run.sh"]
