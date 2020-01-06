FROM centos:6

RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-6.rpm
RUN yum update -y
RUN yum install -y tar wget git unzip maven
RUN yum install -y nginx
RUN yum --enablerepo=remi-php71 install -y php php-mcrypt php-cli php-gd php-curl php-mysql php-ldap php-zip php-fileinfo php-fpm php-mbstring

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY script_start_service.sh script_start_service.sh

RUN ["chmod", "+x", "script_start_service.sh"]

CMD ./script_start_service.sh

EXPOSE 80