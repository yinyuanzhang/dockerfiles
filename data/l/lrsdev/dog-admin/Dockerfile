# See https://github.com/phusion/passenger-docker for base image information
FROM phusion/passenger-ruby22:0.9.17

# Paperclip (image attachment manager) requires imagemagick.
RUN apt-get -y install imagemagick

ENV HOME /root

# Use baseimage-docker's init process
CMD ["/sbin/my_init"]

# Expose Nginx http
EXPOSE 80

# Remove Nginx default site, add our app conf
RUN rm /etc/nginx/sites-enabled/default

# Add nginx site config
ADD ./dockerfiles/docadmin.conf /etc/nginx/sites-enabled/docadmin.conf

# Add env configs
ADD ./dockerfiles/database.conf /etc/nginx/main.d/database.conf
ADD ./dockerfiles/secret_key.conf /etc/nginx/main.d/secret_key.conf
ADD ./dockerfiles/aws.conf /etc/nginx/main.d/aws.conf

# Add SSL certs these are added and terminated at the reverse proxy
# ADD ./files/docadmin.crt /etc/nginx/ssl/docadmin.crt
# ADD ./files/docadmin.key /etc/nginx/ssl/docadmin.key

# Add rails app
ADD . /home/app/docadmin
RUN chown -R app:app /home/app/docadmin

WORKDIR /home/app/docadmin
RUN sudo -u app bundle install --deployment

# Enable Nginx and Passenger
RUN rm -f /etc/service/nginx/down

# Clean up apt
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
