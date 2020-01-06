FROM adolfintel/speedtest
EXPOSE 80
WORKDIR /var/www/html/
RUN mv example-gauges.html index.html
CMD ["/usr/local/bin/apache2-foreground"]