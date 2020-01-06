FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && apt-get install -y --no-install-recommends \
        sqlite3 \
        libsqlite3-dev \
        git \
        build-essential \
        python3.6 \
        python3.6-dev \
        python3-pip \
        python-setuptools \
        cmake \
        curl \
        libsm6 \
        libxext6 \ 
        libxrender-dev

COPY requirements.txt /tmp

WORKDIR /tmp

RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6
RUN python3.6 -m pip install -r requirements.txt

RUN mkdir -p /virtual-assistant/session-manager
ADD .  /virtual-assistant/session-manager
WORKDIR /virtual-assistant/session-manager/src

RUN ./install.sh
 
# CMD ["/virtual-assistant/session-manager"]