FROM eoscanada/eos:v1.0.7

WORKDIR /

# eoskeeper is a python app and the eos image does not bundle python
RUN apt-get -y update && \
    apt-get -y install git python python-pip supervisor vim lsof && \
    pip install sh requests && \
    git clone https://github.com/eosstore/eoskeeper.git

ADD conf/* /

# Set/Expose env vars to create eoskeeper config file.
ENV C_ROLE=$ROLE C_BLOCK_PRODUCER_NAME=$BLOCK_PRODUCER_NAME C_INFLUXDB_URL=$INFLUXDB_URL C_MOBILES=$MOBILES

# Crudely install eoskeeper in the absense of a package for now
RUN cp /eoskeeper/eoskeeper.py /usr/local/bin && \
    chmod +x /usr/local/bin/eoskeeper.py && \
    mkdir /etc/eoskeeper /data && \
    touch /data/eosio.log && \
    echo '[global]' > /etc/eoskeeper/config.ini && \
    echo ' ' >> /etc/eoskeeper/config.ini && \
    echo 'role = '$C_ROLE >> /etc/eoskeeper/config.ini && \
    echo 'block_producer_name = '$C_BLOCK_PRODUCER_NAME >> /etc/eoskeeper/config.ini && \
    echo 'eosio_log_file = /data/eosio.log' >> /etc/eoskeeper/config.ini && \
    echo 'eoskeeper_log_file = /data/eoskeeper.log' >> /etc/eoskeeper/config.ini && \
    echo 'infulxdb_url = '$C_INFLUXDB_URL >> /etc/eoskeeper/config.ini && \
    echo 'mobiles = '$C_MOBILES >> /etc/eoskeeper/config.ini && \
    rm /etc/supervisor/supervisord.conf && \
    mv /supervisord.conf /etc/supervisor/supervisord.conf && \
    chmod +x /start.sh

EXPOSE 8888 9876

CMD ["sh", "-c", "/start.sh"]
