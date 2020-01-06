FROM doalitic/nginx:1.8

MAINTAINER "The Doalitic Team" <devops@doalitic.com>

ADD ./local/doalitic /var/www
RUN chown -R nginx:nginx /var/www

CMD [ "dockerize", \
      "-template", "/etc/container/templates/server.key.tpl:/etc/ssl/private/server.key", \
      "-template", "/etc/container/templates/server.crt.tpl:/etc/ssl/private/server.crt", \
      "-template", "/etc/container/templates/nginx.conf.tpl:/etc/nginx/nginx.conf", \
      "-template", "/var/www/js/contact.js.tpl:/var/www/js/contact.js", \
      "nginx", "-g", "daemon off;" ]
