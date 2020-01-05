FROM marissen/magento2-devops:latest

LABEL maintainer "Marissen timon@marissen.net"

RUN sed -i 's/7.1/7.2/g' /etc/my_init.d/60_restart_services.sh
RUN update-alternatives --set php $(which php7.2)