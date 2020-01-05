FROM akolosov/ubuntu

RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ADD sites-enabled/ /etc/nginx/sites-enabled/
ADD app/ /app/

EXPOSE 80

CMD ["/usr/sbin/nginx"]
