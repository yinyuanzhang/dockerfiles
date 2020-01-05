FROM nginx:latest

MAINTAINER Jamie van Brunschot <jamievbrunschot@gmail.com>

RUN mkdir /templates
RUN rm -v /etc/nginx/conf.d/*.conf

ADD consul-template /usr/bin/
RUN chmod u+x /usr/bin/consul-template
ADD start.sh /bin/start.sh
ADD service.ctmpl /templates/

RUN chmod +x /bin/start.sh

EXPOSE 80
CMD ["/bin/bash", "start.sh"]
