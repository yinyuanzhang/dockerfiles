FROM centos:7
MAINTAINER SFoxDev <admin@sfoxdev.com>

ENV WNHOME=/usr/local/bin

RUN yum -y update \
  && yum -y install gcc make tcl tk curl tar mc \
  && yum groupinstall -y "Development Tools" \
  && yum -y install tk-devel \
  && yum clean all \
  && curl -Lo WNdb-3.0.tar.gz http://wordnetcode.princeton.edu/3.0/WNdb-3.0.tar.gz \
  && tar -xzvf WNdb-3.0.tar.gz -C /usr/local/bin \
  && rm WNdb-3.0.tar.gz \
  && curl -Lo wn3.1.dict.tar.gz http://wordnetcode.princeton.edu/wn3.1.dict.tar.gz \
  && tar -xzvf wn3.1.dict.tar.gz -C /usr/local/bin \
  && rm wn3.1.dict.tar.gz \
  && curl -Lo WordNet-3.0.tar.gz http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz \
  && tar -xzvf WordNet-3.0.tar.gz \
  && rm WordNet-3.0.tar.gz \
  && cd WordNet-3.0 \
  && ./configure --prefix=/usr/local\
  && make \
  && make install

WORKDIR /usr/local/bin

ENTRYPOINT ["/usr/local/bin/wn"]

#CMD ["/bin/bash"]
