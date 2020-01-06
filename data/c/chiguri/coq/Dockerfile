FROM chiguri/coq_base
LABEL maintainer "Sosuke Moriguchi"
ENV CoqVersion=8.7.1
RUN apt-get update && apt-get upgrade -y && \
  wget https://coq.inria.fr/distrib/$CoqVersion/files/coq-$CoqVersion.tar.gz && \
  tar -xzf coq-$CoqVersion.tar.gz && \
  rm -rf coq-$CoqVersion.tar.gz && \
  cd coq-$CoqVersion && \
  ./configure -prefix /usr/local && \
  make && \
  make install && \
  cd .. && \
  rm -rf coq-$CoqVersion
