FROM docker.io/xuhui546/anaconda-centos:3.4.4.0

RUN yum install -y gcc gcc-c++
RUN yum install -y python-devel; yum clean all
RUN yum install -y mysql-devel; yum clean all

# for database
RUN yum install -y freetds*; yum clean all
RUN yum install -y unixODBC*; yum clean all
RUN yum install -y libaio*; yum clean all

RUN yum install -y unzip; yum clean all

RUN mkdir /opt/oracle \
    && cd /opt/oracle \
    && wget https://github.com/strongloop/loopback-oracle-builder/raw/master/deps/oracle/Linux/x64/instantclient-basiclite-linux.x64-12.1.0.2.0.zip \
    && wget https://github.com/strongloop/loopback-oracle-builder/raw/master/deps/oracle/Linux/x64/instantclient-sdk-linux.x64-12.1.0.2.0.zip \
    && unzip /opt/oracle/instantclient-basiclite-linux.x64-12.1.0.2.0.zip -d /opt/oracle \
    && unzip /opt/oracle/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /opt/oracle \
    && ln -s /opt/oracle/instantclient_12_1/libclntsh.so.12.1 /opt/oracle/instantclient_12_1/libclntsh.so \
    && ln -s /opt/oracle/instantclient_12_1/libclntshcore.so.12.1 /opt/oracle/instantclient_12_1/libclntshcore.so \
    && ln -s /opt/oracle/instantclient_12_1/libocci.so.12.1 /opt/oracle/instantclient_12_1/libocci.so \
    && rm -rf /opt/oracle/*.zip

ENV LD_RUN_PATH /opt/oracle/instantclient_12_1
ENV ORACLE_HOME /opt/oracle/instantclient_12_1
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_12_1

RUN pip install \
    pymysql\
    mysqlclient\
    celery\
    Django\
    django-autocomplete-light\
    django-bootstrap3\
    django-celery-results\
    django-celery-beat\
    django-cors-headers\
    django-crispy-forms\
    django-downloadview\
    django-extensions\
    django-filter\
    django-guardian\
    django-import-export\
    django-mptt\
    django-pandas\
    django-redis\
    djangorestframework\
    djangorestframework-jwt\
    django-userena\
    python-social-auth\
    uWSGI\
    cx-Oracle\
    elasticsearch\
    redis
