FROM muhlisbc/docker-ruby-mongodb

MAINTAINER Muhlis BC "muhlisbc@gmail.com"

ENV RAILS_LOG_TO_STDOUT=1 \
	RAILS_ENV=production

WORKDIR /app

COPY . /app

RUN rm -f /etc/nginx/*ed/* \
	&& mv nginx_vhost.conf /etc/nginx/*ed/ \
	&& echo "gem: --no-document" >> $HOME/.gemrc \
	&& bundle \
	&& rake assets:precompile \
	&& rm -rf /var/lib/apt/lists/* /tmp/* \
	&& mkdir -p /data/db /data/configdb \
	&& chown -R mongodb:mongodb /data/db /data/configdb

EXPOSE 80 27017

CMD bash /app/start.sh
