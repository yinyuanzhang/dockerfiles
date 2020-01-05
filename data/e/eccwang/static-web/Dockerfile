# Version: 0.0.1
FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
	nginx \
	supervisor \
	wget \
	curl
#RUN echo 'Hi, I am in your container.' > /usr/share/nginx/html/index.html
EXPOSE 80

ADD start.sh /usr/local/bin/start.sh
RUN chmod -v +x /usr/local/bin/start.sh

ADD supervisord.conf /etc/supervisord.conf

CMD ["/usr/local/bin/start.sh"]
#ENTRYPOINT ["nginx"]

#CMD ["-g", "daemon off;"]
