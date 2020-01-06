FROM tarscloud/tars:dev
MAINTAINER goshja goshja <goshja@qq.com>
RUN yum update -y
#RUN yum install -y php-swoole &&\
#    #禁用老的swoole 2.0
#    sed -i "s/extension=swoole.so/;extension=swoole.so/" /etc/php.d/swoole.ini
RUN sed -i "s/;date.timezone =/date.timezone = Asia\/Shanghai;/" /etc/php.ini
RUN composer config -g repo.packagist composer https://packagist.phpcomposer.com
RUN ln -s /usr/local/app/tars/tarsnode/data /deployed
RUN ln -s /usr/local/app/tars/app_log/ /app_log
RUN yum -y install kde-l10n-Chinese telnet && \
    yum -y reinstall glibc-common &&\
    yum clean all  && \
    localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
RUN yum install -y php-redis php-dom php-bcmath
RUN yum install -y net-tools