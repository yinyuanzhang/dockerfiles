FROM	rabbitmq:3.7.7

# Enable the delay message plugin for RabbitMQ, along with the management plugin.
RUN	apt-get update
RUN	apt-get -y install curl unzip

RUN	mkdir /usr/lib/rabbitmq/plugins
RUN	curl -O https://dl.bintray.com/rabbitmq/community-plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
RUN	unzip rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
RUN	mv rabbitmq_delayed_message_exchange-20171201-3.7.x.ez /usr/lib/rabbitmq/plugins/
RUN	rabbitmq-plugins enable rabbitmq_delayed_message_exchange
RUN	rabbitmq-plugins enable rabbitmq_management


EXPOSE	4369
EXPOSE	5672
EXPOSE	5671
EXPOSE	15672
