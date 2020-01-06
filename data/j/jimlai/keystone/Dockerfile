from ubuntu:14.04

MAINTAINER jimlai Jim.Lai@qcttw.com.tw

#ENV http_proxy="http://192.168.89.200:3128"
#ENV https_proxy="https://192.168.89.200:3128"
ENV RABBIT_USER=openstack
ENV RABBIT_PASS=123
ENV MYSQL_PASS=123
ENV PASS=123
ENV HOSTNAME=controller
ENV ADMIN_TOKEN=123

# update first to get cloud keyring, set dist-selection as kilo, also grab nano git curl pip ... as foundation tools
RUN apt-get update && apt-get install -y ubuntu-cloud-keyring keystone python-openstackclient nano git curl && \  
	echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-updates/kilo main" > \
        /etc/apt/sources.list.d/cloudarchive-kilo.list && \
        curl "https://bootstrap.pypa.io/get-pip.py" -o "/get-pip.py" && /usr/bin/python /get-pip.py 

# separated install stages so as to NOT re-install everything when something went wrong
RUN apt-get install -y rabbitmq-server apache2 
RUN apt-get install -y libapache2-mod-wsgi memcached python-memcache
RUN apt-get install -y python-mysqldb python-dev

# update again to reflect kilo dist-selection, then dist-upgrade
RUN apt-get update && apt-get -y dist-upgrade 

# setup rabbitmq user password
RUN service rabbitmq-server start && rabbitmqctl add_user $RABBIT_USER $RABBIT_PASS && rabbitmqctl \
                       set_permissions $RABBIT_USER ".*" ".*" ".*" 


# install mariadb and set up password without interactions 
RUN export DEBIAN_FRONTEND=noninteractive
RUN /bin/bash -c "debconf-set-selections <<< 'mariadb-server-5.5 mysql-server/root_password password $MYSQL_PASS'"
RUN /bin/bash -c "debconf-set-selections <<< 'mariadb-server-5.5 mysql-server/root_password_again password $MYSQL_PASS'" 
RUN apt-get -y install mariadb-server  
	  
# only use bash, override not needed, to be removed later
RUN echo "manual" > /etc/init/keystone.override
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# setup DB
RUN echo "CREATE DATABASE keystone; GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' \
                                IDENTIFIED BY '$PASS'; GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' \
                                IDENTIFIED BY '$PASS';" > /keystone.db
RUN service mysql start && mysql -u root -p$MYSQL_PASS < /keystone.db


# config keystone
RUN sed  -i "/admin_token/c\admin_token = $ADMIN_TOKEN" /etc/keystone/keystone.conf
RUN sed  -i "/connection = sqlite/c\connection = mysql://keystone:$PASS@$HOSTNAME/keystone" /etc/keystone/keystone.conf
RUN sed  -i '/servers=localhost/c\servers = localhost:11211' /etc/keystone/keystone.conf
RUN sed  -i '/provider=/c\provider = keystone.token.providers.uuid.Provider' /etc/keystone/keystone.conf
RUN sed  -i '/driver=keystone.token/c\driver = keystone.token.persistence.backends.memcache.Token' /etc/keystone/keystone.conf
RUN sed  -i '/driver=keystone.contrib.revoke/c\driver = keystone.contrib.revoke.backends.sql.Revoke' /etc/keystone/keystone.conf
RUN sed  -i '/verbose=/c\verbose = true' /etc/keystone/keystone.conf


# config mysql
RUN nl=$'\n' && echo "[mysqld] $nl bind-address = $HOSTNAME $nl default-storage-engine = innodb $nl  innodb_file_per_table $nl \
          collation-server = utf8_general_ci $nl init-connect = 'SET NAMES utf8' $nl character-set-server = utf8" \
                > /etc/mysql/conf.d/mysqld_openstack.cnf


# populate database
RUN echo $(head -1 /etc/hosts | cut -f1) $HOSTNAME >> /etc/hosts && \
    service mysql start && \
    keystone-manage db_sync

# config apache
RUN echo "ServerName $HOSTNAME" >> /etc/apache2/apache2.conf
RUN nl=$'\n' && echo " \
Listen 5000 $nl \
Listen 35357 $nl \

<VirtualHost *:5000> $nl \
    WSGIDaemonProcess keystone-public processes=5 threads=1 user=keystone display-name=%{GROUP} $nl \
    WSGIProcessGroup keystone-public $nl \
    WSGIScriptAlias / /var/www/cgi-bin/keystone/main $nl\
    WSGIApplicationGroup %{GLOBAL} $nl\
    WSGIPassAuthorization On $nl\
    <IfVersion >= 2.4> $nl \
      #ErrorLogFormat "%{cu}t %M" $nl\
    </IfVersion> $nl \
    LogLevel info $nl \
    ErrorLog /var/log/apache2/keystone-error.log $nl \
    CustomLog /var/log/apache2/keystone-access.log combined $nl \
</VirtualHost> $nl \
$nl \
<VirtualHost *:35357> $nl\
    WSGIDaemonProcess keystone-admin processes=5 threads=1 user=keystone display-name=%{GROUP} $nl\
    WSGIProcessGroup keystone-admin $nl\
    WSGIScriptAlias / /var/www/cgi-bin/keystone/admin $nl\
    WSGIApplicationGroup %{GLOBAL} $nl\
    WSGIPassAuthorization On $nl \
    <IfVersion >= 2.4> $nl\
      #ErrorLogFormat "%{cu}t %M" $nl\
    </IfVersion> $nl\
    LogLevel info $nl\
    ErrorLog /var/log/apache2/keystone-error.log $nl\
    CustomLog /var/log/apache2/keystone-access.log combined $nl\
</VirtualHost> "  > /etc/apache2/sites-available/wsgi-keystone.conf

RUN ln -s /etc/apache2/sites-available/wsgi-keystone.conf /etc/apache2/sites-enabled
RUN mkdir -p /var/www/cgi-bin/keystone
RUN curl http://git.openstack.org/cgit/openstack/keystone/plain/httpd/keystone.py?h=stable/kilo \
  | tee /var/www/cgi-bin/keystone/main /var/www/cgi-bin/keystone/admin
RUN chown -R keystone:keystone /var/www/cgi-bin/keystone
RUN chmod 755 /var/www/cgi-bin/keystone/*

# ports to expose
EXPOSE 22 80 3306 5000 35357



# setup services and endpoints 
RUN echo $(head -1 /etc/hosts | cut -f1) $HOSTNAME >> /etc/hosts && \ 
   service apache2 start && \
   service mysql start && \
   export OS_TOKEN=$PASS && \ 
   export OS_URL=http://$HOSTNAME:35357/v2.0 && \
   unset http_proxy && \
   unset https_proxy && \
   openstack service create --description "OpenStack Identity" --name keystone identity && \
   openstack endpoint create \
  --publicurl http://controller:5000/v2.0 \
  --internalurl http://controller:5000/v2.0 \
  --adminurl http://controller:35357/v2.0 \
  --region RegionOne identity && \
  openstack project create --description "Admin Project" admin && \
  openstack user create --password $PASS admin && \
  openstack role create admin && \
  openstack role add --project admin --user admin admin && \
  openstack project create --description "Service Project" service  && \
  openstack project create --description "Demo Project" demo && \
  openstack user create --password $PASS demo && \
  openstack role create user && \
  openstack role add --project demo --user demo user

# create client environment scripts
RUN nl=$'\n' && echo "export OS_PROJECT_DOMAIN_ID=default $nl export OS_USER_DOMAIN_ID=default $nl export OS_PROJECT_NAME=admin \
 $nl export OS_TENANT_NAME=admin $nl export OS_USERNAME=admin $nl export OS_PASSWORD=$PASS $nl \
 export OS_AUTH_URL=http://controller:35357/v3" > /admin-openrc.sh && echo "export OS_PROJECT_DOMAIN_ID=default $nl \
export OS_USER_DOMAIN_ID=default $nl export OS_PROJECT_NAME=demo $nl export OS_TENANT_NAME=demo $nl export OS_USERNAME=demo $nl \
export OS_PASSWORD=$PASS $nl export OS_AUTH_URL=http://controller:5000/v3" > /demo-openrc.sh

# setup sshd, note that it uses root login with password $PASS
RUN apt-get install -y openssh-server
RUN ssh-keygen -A && mkdir /var/run/sshd && sed -i "/PermitRootLogin/c\PermitRootLogin yes" /etc/ssh/sshd_config && \
    echo root:$PASS | /usr/sbin/chpasswd

# init script to start all container services
RUN nl=$'\n' && echo "#!/bin/bash $nl source admin-openrc.sh $nl unset http_proxy $nl service mysql start $nl \
    service rabbitmq-server start & $nl service apache2 start $nl /usr/sbin/sshd & $nl tail -f /dev/null" > /init && chmod +x /init 

CMD /bin/bash





