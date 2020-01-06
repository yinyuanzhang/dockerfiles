FROM shkatara/firstrepo:first_docker_cloud_image
COPY index.html /var/www/html/index.html
RUN yum install net-tools -y 
EXPOSE 80
ENTRYPOINT ["/usr/sbin/httpd","-DFOREGROUND"]
