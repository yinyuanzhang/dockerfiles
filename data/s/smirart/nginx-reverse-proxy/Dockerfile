FROM nginx

# deamon mode off
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf


#VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/var/log/nginx"]

# expose ports
EXPOSE 80 443

WORKDIR /etc/nginx
CMD ["nginx"]
