FROM amazonlinux:2017.09
MAINTAINER @mathetake

ENV PYTHONVER 3.6.1

RUN yum -y install make
RUN yum -y install gcc
RUN yum -y install zlib-devel
RUN yum -y install bzip2-devel
RUN yum -y install openssl-devel
RUN yum -y install ncurses-devel
RUN yum -y install sqlite-devel
RUN yum -y install readline-devel
RUN yum -y install wget
RUN yum -y install zip

WORKDIR /tmp

RUN wget --no-check-certificate https://www.python.org/ftp/python/${PYTHONVER}/Python-${PYTHONVER}.tgz
RUN tar -zxvf Python-${PYTHONVER}.tgz

WORKDIR /tmp/Python-${PYTHONVER}
RUN ./configure --prefix=/usr/local
RUN make && make altinstall

RUN yum clean all
RUN rm -rf /tmp/Python-${PYTHONVER}

WORKDIR /root
RUN unlink /usr/bin/python
RUN ln -s /usr/local/bin/python3.6 /usr/bin/python
RUN ln -s /usr/local/bin/pip3.6 /usr/bin/pip

RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install tensorflow
RUN pip install keras
RUN pip install awscli
