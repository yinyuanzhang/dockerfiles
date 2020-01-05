FROM joaolboing/apache-php5

ENV DEBIAN_FRONTEND=newt

ADD apache2.conf /etc/apache2/apache2.conf

RUN apt-get update && \
apt-get install -y php5-xdebug multitail screen && \

echo "xdebug.remote_enable=on" >> /etc/php5/apache2/conf.d/20-xdebug.ini && \
echo "xdebug.remote_autostart=off" >> /etc/php5/apache2/conf.d/20-xdebug.ini && \

sed -i 's/^error_reporting = .*/error_reporting = E_ALL/' /etc/php5/apache2/php.ini && \

rm -rf /var/lib/apt/lists/*

#RUN ln -sf /dev/stdout /var/log/apache2/access.log
RUN ln -sf /dev/stdout /var/log/apache2/error.log
