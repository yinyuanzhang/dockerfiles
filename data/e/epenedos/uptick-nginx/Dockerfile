FROM nginx

# Run apt-get update
RUN apt-get update

# Install Git
RUN apt-get install -y git 

RUN mkdir -p /var/www/html
WORKDIR /var/www/html/

RUN git clone https://github.com/epenedos/Uptick-NGINX.git
RUN cp -rf /var/www/html/Uptick-NGINX/* /var/www/html/

RUN chmod -R 755 /var/www/html/*
RUN sed -i 's/\/usr\/share\/nginx\/html/\/var\/www\/html/g' /etc/nginx/conf.d/default.conf







