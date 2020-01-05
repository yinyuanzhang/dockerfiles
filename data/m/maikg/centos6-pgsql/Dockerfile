FROM maikg/centos6-wget

RUN rm -f /tmp/pgsql-repo.rpm

RUN wget -O /tmp/pgsql-repo.rpm https://yum.postgresql.org/9.4/redhat/rhel-6-i386/pgdg-redhat94-9.4-3.noarch.rpm

RUN yum -y localinstall /tmp/pgsql-repo.rpm

RUN yum -y install postgresql94-server
