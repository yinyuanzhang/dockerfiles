FROM python:3.6

#Install uwsgi and django
RUN pip install --no-cache-dir uwsgi django

# setup all the configfiles
COPY config/uwsgi.ini /config/

#Create source directory
RUN mkdir -p /home/django/app && chown -R www-data:www-data /home/django/app

WORKDIR /home/django

EXPOSE 8080
CMD ["/usr/local/bin/uwsgi", "--ini", "/config/uwsgi.ini"]
