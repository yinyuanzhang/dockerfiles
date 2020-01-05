FROM ubuntu:18.04
RUN apt-get update -qq
RUN apt-get install -y nginx curl
RUN echo 'lunchtime' >  /var/www/html/index.nginx-debian.html
ENV TITLE=Welcome
ENV BODY="Please use BODY/TITLE/COLOR env variables"
ENV COLOR=lightblue
COPY start.sh /
RUN chmod +x /start.sh
EXPOSE 80
CMD /start.sh
