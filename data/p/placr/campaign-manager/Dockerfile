FROM      node:0.10

# Update system
RUN \
          apt-get update && \
          apt-get install -y nginx git && \
          rm -rf /var/lib/apt/lists/*

COPY      docker-entrypoint.sh /

# Add Campaign manager application
RUN       mkdir -p /var/www/cm/

COPY      . /source/

WORKDIR   /source/

RUN       npm install -g grunt-cli bower
RUN       npm install
RUN       bower install --allow-root --config.interactive=false
RUN       grunt build

RUN       mv dist/* /var/www/cm/ && mv /var/www/ /var/www1/ && mv /var/www1/ /var/www/
RUN       chown -R www-data:www-data /var/www/cm/

COPY      nginx.conf /etc/nginx/sites-enabled/cm.conf
RUN       rm /etc/nginx/sites-enabled/default

EXPOSE    80

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD       ["nginx", "-g", "daemon off;"] 