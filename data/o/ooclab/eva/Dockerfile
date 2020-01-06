FROM ubuntu
MAINTAINER lijian@ooclab.com

ENV PATH /usr/local/bin:$PATH
#ENV LANG en_US.UTF-8

RUN apt-get update -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y python3 curl net-tools iputils-ping python3-nose vim ipython3 python3-pip \
           build-essential python3-dev libssl-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pip --upgrade
RUN pip3 install wheel python-dateutil tornado sqlalchemy six wtforms
# https://pypi.python.org/pypi/pyeva
RUN pip3 install https://pypi.python.org/packages/93/c9/0e0cd24f733dae1276ef818e2f12d504c7ef5630822ab9f639fbc5e385e0/pyeva-2.2.1.tar.gz#md5=454a1d84b69e68de03f27e9b7069cbfb

VOLUME /work
WORKDIR /work

CMD ["bash"]
