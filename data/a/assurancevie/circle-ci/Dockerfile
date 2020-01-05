FROM circleci/php:7.3.7-node

RUN sudo docker-php-ext-install bcmath
RUN sudo docker-php-ext-install pdo_mysql
RUN sudo docker-php-ext-install sockets
RUN echo "[Date]\ndate.timezone = Europe/Paris\n[Memory]\nmemory_limit = -1" | sudo tee /usr/local/etc/php/php.ini > /dev/null
RUN sudo mkdir -p /var/lib/php/sessions

RUN sudo apt-get update && sudo apt-get install pdftk

RUN \
  echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list && \
  wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add - && \
  sudo apt-get update && \
  sudo apt-get install rabbitmq-server && \
  sudo rabbitmq-plugins enable rabbitmq_management

RUN \
  cd /tmp && \
  wget https://github.com/corvus-ch/rabbitmq-cli-consumer/releases/download/2.2.0/rabbitmq-cli-consumer_2.2.0_linux_amd64.tar.gz && \
  sudo tar xfzv rabbitmq-cli-consumer_2.2.0_linux_amd64.tar.gz && \
  sudo mv rabbitmq-cli-consumer /usr/local/bin/

EXPOSE 5672
