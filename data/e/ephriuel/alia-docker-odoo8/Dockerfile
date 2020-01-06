# Dockerfile
FROM ubuntu:14.04
MAINTAINER Loxo Lueiro Astray

# Set the locale
RUN locale-gen es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES:es
ENV LC_ALL es_ES.UTF-8

# Install dependencies
RUN sh -c "echo 'deb http://apt.anybox.fr/openerp common main' >> /etc/apt/sources.list.d/openerp.list"
RUN apt-get update
RUN apt-get install -y --force-yes openerp-server-system-build-deps \
		libffi-dev \
		python-dev \
		libpq-dev \
		libreadline-dev		

# Install pip and virtualenv
RUN apt-get install -y --force-yes python-pip
RUN pip install virtualenv

# Create new user alia
RUN adduser --home=/home/alia --disabled-password --gecos "" --shell=/bin/bash alia

# Install wkhtmltopdf
#RUN curl -o wkhtmltox.deb -SL http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb \
#        && echo '40e8b906de658a2221b15e4e8cd82565a47d7ee8 wkhtmltox.deb' | sha1sum -c - \
#        && dpkg --force-depends -i wkhtmltox.deb \
#        && apt-get -y install -f --no-install-recommends \
#        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false npm \
#        && rm -rf /var/lib/apt/lists/* wkhtmltox.deb

# Log as alia        
USER alia
ENV HOME /home/alia

# Create odoo directory
RUN mkdir /home/alia/odoo8
WORKDIR /home/alia/odoo8

# Add buildout config files
ADD . /home/alia/odoo8

# Create virtual environment
RUN virtualenv /home/alia/odoo8

# Run bootstrap
RUN /home/alia/odoo8/bin/python /home/alia/odoo8/bootstrap.py

# Execute buildout 
RUN /home/alia/odoo8/bin/buildout

EXPOSE 8069
