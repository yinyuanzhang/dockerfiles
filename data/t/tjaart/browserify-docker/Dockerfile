# An image that has nginx and node+npm installed
#
# I use the image to deploy webapps built with browserify. Simply copy the  browserified code into:
# /usr/share/nginx/html/

FROM nginx
MAINTAINER Tjaart van der Walt <docker@tjaart.co.za>

RUN apt-get -yq update && \
    apt-get upgrade -yq && \ 
    apt-get install -yq curl && \
    curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
    apt-get -qq -y install nodejs && \
    apt-get -qq -y install git && \
    rm -r /usr/share/nginx/html/*
