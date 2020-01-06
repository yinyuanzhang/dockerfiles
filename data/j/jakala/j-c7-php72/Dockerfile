FROM jakala/j-c7:latest
MAINTAINER noc@jakala.com
RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.4.3-x86_64.rpm && rpm -vi filebeat-5.4.3-x86_64.rpm && rm -f filebeat-5.4.3-x86_64.rpm
RUN yum -y install https://$(rpm -E '%{?centos:centos}%{!?centos:rhel}%{rhel}').iuscommunity.org/ius-release.rpm && \
	yum -y install httpd mod_php72u php72u-mbstring php72u-fpm php72u-gd php72u-xml php72u-pdo php72u-zip php72u-pgsql php72u-opcache php72u-json php72u-cli && \
	yum clean all
COPY etc /etc/
COPY DATA/ /DATA/
ADD apachectl.sh /
COPY etc/filebeat/filebeat.yml /etc/filebeat/filebeat.yml 
CMD [ "/apachectl.sh" ]