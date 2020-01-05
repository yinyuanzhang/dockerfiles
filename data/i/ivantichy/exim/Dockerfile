FROM debian:jessie

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      exim4 \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
  
  COPY ./entrypoint.sh /entrypoint.sh
  COPY ./update-exim4.conf.conf /etc/exim4/update-exim4.conf.conf
  
  RUN update-exim4.conf
  
  EXPOSE 25
  
  ENTRYPOINT [ "/entrypoint.sh" ] 
