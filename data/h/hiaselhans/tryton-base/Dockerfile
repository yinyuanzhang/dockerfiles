# Trytond 3.2
#
# * Also installs postgres-9.3, the recommended database engine
#
# VERSION	3.2.0.1

FROM centos

# Update package repository, pip
RUN yum -y update
RUN yum -y install python-setuptools
RUN easy_install pip
# make the terminal prettier
RUN echo 'export PS1="[\u@docker] \W # "' >> /root/.bash_profile



# Setup environment and UTF-8 locale
#ENV DEBIAN_FRONTEND noninteractive
#ENV LANGUAGE en_US.UTF-8
#ENV LANG en_US.UTF-8
#ENV LC_ALL en_US.UTF-8
#RUN apt-get -y -q install language-pack-en-base
#RUN locale-gen en_US.UTF-8
#RUN dpkg-reconfigure locales

# TRYTON deps
RUN yum -y install python-psycopg2 python-lxml
RUN pip2 install relatorio genshi python-dateutil polib python-sql

EXPOSE 	8000 22
