FROM nginx:1.16.0 

COPY nginx-reload.sh /opt/nginx-reload.sh
RUN chmod +x /opt/nginx-reload.sh

ADD rewrite /etc/nginx/rewrite/

RUN apt-get update -y && apt-get install -y inotify-tools

CMD ["/opt/nginx-reload.sh"]