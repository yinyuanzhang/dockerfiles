FROM meanbee/magento:7.2-cli

RUN apt-get update && apt-get install -y redis-tools \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD entrypoint.sh /entrypoint.sh
