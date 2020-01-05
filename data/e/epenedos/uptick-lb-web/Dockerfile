FROM nginx
# Run apt-get update
RUN apt-get update

# Install Git
RUN apt-get install -y git 

RUN mkdir -p /var/www/projects
WORKDIR /var/www/projects
RUN git clone https://github.com/epenedos/Uptick-LB-Web
RUN mv /var/www/projects/Uptick-LB-Web/load-balancer.conf /etc/nginx/conf.d/load-balancer.conf
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled

