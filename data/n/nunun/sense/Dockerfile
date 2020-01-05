FROM million12/kibana4

RUN /opt/kibana/bin/kibana plugin --install elastic/sense
ADD kibana.yml /opt/kibana/config/kibana.yml

RUN rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
RUN yum install -y nginx
ADD nginx.conf /etc/nginx/conf.d/default.conf

ADD bootstrap.sh /bootstrap.sh
RUN chmod 775 /bootstrap.sh
