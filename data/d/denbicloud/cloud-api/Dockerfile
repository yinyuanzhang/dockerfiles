FROM debian:stretch

MAINTAINER deNBI.de

# Domain to use
ARG DOMAIN
ENV DOMAIN=$DOMAIN

# Django settings to use
ARG SETTINGS="djfront.settings_staging"
ENV SETTINGS=$SETTINGS

ENV SECRET_KEY="default"

ENV OIDC_CLIENT_ID="default"

ENV OIDC_CLIENT_SECRET="default"

ENV OIDC_SIGN_KEY="default"

ENV SERVICE_USER_LOGIN="default"

ENV SERVICE_USER_PASSWORD="default"

ENV DJANGO_SETTINGS_MODULE=$SETTINGS

#Install required software
RUN apt-get update --fix-missing \
    && apt install -y git apache2 python3 python3-pip libapache2-mod-wsgi-py3 curl locales vim libpq-dev
RUN curl -L -O https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    #Configure apache
    && a2enmod ssl \
    && a2enmod wsgi \
    && service apache2 restart
ADD /app/requirements.txt /tmp/requirements.txt

# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

#create virtualenv
RUN pip3 install -r /tmp/requirements.txt

# add Django APP
ADD /app /var/www

#insert main template into django
ADD /app/static/webapp/assets /var/www/static/webapp/assets

ADD entrypoint.sh /entrypoint.sh

#fix callback in mozilla django oidc plugin views.py
ADD views.patch /usr/local/lib/python3.5/dist-packages/mozilla_django_oidc/views.patch
WORKDIR /usr/local/lib/python3.5/dist-packages/mozilla_django_oidc
RUN patch <views.patch
ADD django.contrib.auth.admin.patch /usr/local/lib/python3.5/dist-packages/django/contrib/auth/admin.patch
ADD django.contrib.auth.forms.patch /usr/local/lib/python3.5/dist-packages/django/contrib/auth/forms.patch
WORKDIR /usr/local/lib/python3.5/dist-packages/django/contrib/auth
RUN patch < forms.patch
RUN patch < admin.patch



#migrate and start apache
WORKDIR /var/www/
RUN chown www-data. .
