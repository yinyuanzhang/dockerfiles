FROM rabbitmq:3.7.17

RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		curl \
        ca-certificates \
        unzip \
	; \
	rm -rf /var/lib/apt/lists/*; 

RUN mkdir -p /opt/rabbitmq/plugins; \
    cd /tmp; \
    curl -LO 'https://dl.bintray.com/rabbitmq/community-plugins/3.7.x/rabbitmq_lvc_exchange/rabbitmq_lvc_exchange-20171201-3.7.x.zip'; \
    unzip rabbitmq_lvc_exchange-20171201-3.7.x.zip; \
    rm rabbitmq_lvc_exchange-20171201-3.7.x.zip; \
    mv rabbitmq_lvc_exchange-20171201-3.7.x.ez /opt/rabbitmq/plugins/rabbitmq_lvc_exchange-3.7.17.ez;



    