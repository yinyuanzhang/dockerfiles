FROM python:3

RUN apt-get update -y && apt-get dist-upgrade -y && apt-get autoremove --purge -y && apt-get autoclean -y

RUN wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.25-linux-glibc2.12-x86_64.tar.gz &&\
    tar xf mysql-5.7.25-linux-glibc2.12-x86_64.tar.gz &&\
    rm -rf mysql-5.7.25-linux-glibc2.12-x86_64.tar.gz &&\
    mv mysql-5.7.25-linux-glibc2.12-x86_64 mysql

WORKDIR /backup

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV MYSQLDUMP_COMMAND /mysql/bin/mysqldump
ENV DATABASE_URL mysql://mysql@localhost/mysql
ENV FTP_URL ftp://backup:password@backup.network/backups/mydb
VOLUME /tmp

COPY backup.py .
CMD python /backup/backup.py
