FROM debian:latest

# File Author / Maintainer
MAINTAINER HybridGorilla

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential \
    python \
    python-dev\
    python-pip \
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

# Copy over and install the requirements
COPY ./app/requirements.txt /var/www/Orwell/app/requirements.txt
RUN pip install -r /var/www/Orwell/app/requirements.txt

# Copy over the apache configuration file and enable the site
COPY ./Orwell.conf /etc/apache2/sites-available/Orwell.conf
RUN a2ensite Orwell
RUN a2enmod headers

# Copy over the wsgi file
COPY ./Orwell.wsgi /var/www/Orwell/Orwell.wsgi

COPY ./run.py /var/www/Orwell/run.py
COPY ./app /var/www/Orwell/app/
RUN mkdir /tmp/EXT_FOLDER
RUN chmod 777 /tmp/EXT_FOLDER

RUN a2dissite 000-default.conf
RUN a2ensite Orwell.conf

EXPOSE 80

WORKDIR /var/www/Orwell

# CMD ["/bin/bash"]
CMD  /usr/sbin/apache2ctl -D FOREGROUND
# The commands below get apache running but there are issues accessing it online
# The port is only available if you go to another port first
# ENTRYPOINT ["/sbin/init"]
# CMD ["/usr/sbin/apache2ctl"]
