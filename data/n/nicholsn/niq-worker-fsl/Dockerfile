FROM nicholsn/niquery
MAINTAINER Nolan Nichols <orcid.org/0000-0003-1099-3328>
ENV UPDATED "Sun Aug 24 11:28:22 PDT 2014"

RUN \
  wget -O- http://neuro.debian.net/lists/trusty.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list && \
  apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 2649A5A9 && \
  apt-get update && \
  apt-get -y install fsl && \
  echo "source /etc/fsl/5.0/fsl.sh" >> ~/.bashrc

ADD run.sh run.sh
RUN chmod +x run.sh
CMD ./run.sh
