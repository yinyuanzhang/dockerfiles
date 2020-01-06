FROM ggrandes/ubuntu32:14.04 

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -yqq apache2 php5 php-auth php5-mysql php5-odbc && \
    apt-get install -yqq gcc daemon git mysql-server libmyodbc && \
    apt-get install -yqq unixodbc unixodbc-dev stunnel4 && \
    apt-get install -yqq iptables 

RUN groupadd -g 1234 openqwaq && \
    useradd -g 1234 -G 1234 -u 1234 -c "OpenQwaq service user" -d /home/openqwaq -m -s /bin/bash openqwaq && \
    echo "openqwaq:openqwaq" | chpasswd

RUN adduser openqwaq sudo

#USER openqwaq
WORKDIR /home
RUN rm -rf openqwaq
RUN git clone https://github.com/OpenFora/openqwaq.git
RUN ln -s /home/openqwaq/server/etc/OpenQwaq-http.conf /etc/apache2/sites-available/OpenQwaq-http.conf
RUN sed -i 's/www-data/openqwaq/g' /etc/apache2/envvars 
RUN chown -R openqwaq:openqwaq /home/openqwaq
RUN chmod 750 /home/openqwaq
RUN a2enmod proxy && a2enmod proxy_http && a2enmod rewrite && \
    a2enmod auth_digest 
RUN a2ensite OpenQwaq-http 
RUN service apache2 restart

#Database setup
WORKDIR /home/openqwaq/server/conf
RUN ln -s /usr/lib/i386-linux-gnu/odbc/libmyodbc.so /usr/lib/libmyodbc.so

RUN service mysql start && \
    /usr/bin/mysqladmin -u root password openqwaq && \
    /usr/bin/mysql -uroot -popenqwaq -b < ./mysqlinit.sql
RUN odbcinst -i -s -l -f ./OpenQwaqData.dsn.in && \
    odbcinst -i -s -l -f ./OpenQwaqActivityLog.dsn.in && \
    cp ../etc/OpenQwaq-odbcinst.ini /etc/odbcinst.ini
RUN service mysql start && \
    isql OpenQwaqData openqwaq openqwaq -b < ./OpenQwaqData.sql && \
    isql OpenQwaqActivityLog openqwaq openqwaq -b < ./OpenQwaqActivityLog.sql && \
    isql OpenQwaqData openqwaq openqwaq -b < ./default-servers.sql && \
    isql OpenQwaqData openqwaq openqwaq -b < ./default-visitor.sql
RUN cp /home/openqwaq/server/conf/server.conf.in /home/openqwaq/server/conf/server.conf
RUN mkdir /home/openqwaq/realms && \
    cp /home/openqwaq/server/etc/forums.properties /home/openqwaq/realms/ && \
    ln -s /home/openqwaq/server/system-resources/ /home/openqwaq/realms/ && \
    ln -s /home/openqwaq/server/etc/OpenQwaq /etc/init.d/ && \
    ln -s /home/openqwaq/server/etc/OpenQwaq-iptables /etc/init.d/ && \
    ln -s /home/openqwaq/server/etc/OpenQwaq-tunnel /etc/init.d/
RUN sed -i 's=/etc/init.d/init-functions=/lib/lsb/init-functions=g' /home/openqwaq/server/etc/OpenQwaq && \
    sed -i 's=/etc/init.d/init-functions=/lib/lsb/init-functions=g' /home/openqwaq/server/etc/OpenQwaq-iptables && \
    sed -i 's=/etc/init.d/init-functions=/lib/lsb/init-functions=g' /home/openqwaq/server/etc/OpenQwaq-tunnel
RUN a2dissite 000-default
WORKDIR /home/openqwaq/server/etc
RUN chmod 775 OpenQwaq && \
    chmod 775 OpenQwaq-iptables && \
    chmod 775 OpenQwaq-tunnel && \
    chmod 775 /home/openqwaq/server/foreign-client-proxy/LaunchProxy && \
    chown -R openqwaq:openqwaq /home/openqwaq
RUN apt-get install gpac libgpac-dev && ln -s /usr/bin/MP4Box /usr/local/bin/MP4Box
RUN cp ld.so.conf.d/OpenQwaq-mp4box.conf /etc/ld.so.conf.d
#RUN apt-get install zlib1g-dev make
#RUN ../third-party/src/GPAC/run_me_build_mp4box.sh
#RUN service OpenQwaq start

