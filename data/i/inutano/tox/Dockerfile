FROM ubuntu:zesty

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update -y && \
    apt-get install -y libssl1.0.0 git python python-pip python-dev build-essential

RUN pip install tox-travis

CMD ["bash"]