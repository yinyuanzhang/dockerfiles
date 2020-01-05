FROM debian:latest

MAINTAINER badhombres

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential \
    python \
    python-dev\
    python-pip \
    vim \
    sqlite3 \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

# Copy over and install the requirements
COPY ./app/requirements.txt /var/www/CTF/app/requirements.txt
RUN pip install -r /var/www/CTF/app/requirements.txt

# Copy over the apache configuration file and enable the site
COPY ./CTF.conf /etc/apache2/sites-available/CTF.conf
RUN a2ensite CTF
RUN a2enmod headers

# Copy over the wsgi file
COPY ./CTF.wsgi /var/www/CTF/CTF.wsgi

COPY ./run.py /var/www/CTF/run.py
COPY ./app /var/www/CTF/app/
COPY ./sql/schema.sql /tmp/schema.sql
RUN  sqlite3 /var/www/CTF/app/users.db < /tmp/schema.sql

RUN a2dissite 000-default.conf
RUN a2ensite CTF.conf

RUN chown -R www-data:www-data /var/www/CTF/app

COPY ./secrets /var/www/CTF/secrets
RUN chown -R www-data:www-data /var/www/CTF/secrets

EXPOSE 80

WORKDIR /var/www/CTF

CMD  /usr/sbin/apache2ctl -D FOREGROUND
