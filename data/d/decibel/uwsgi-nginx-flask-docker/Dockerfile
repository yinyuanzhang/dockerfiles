FROM tiangolo/uwsgi-nginx:python3.7-alpine3.9

LABEL maintainer="Giuseppe Broccolo <gbroccolo@decibelinsight.com>"

RUN pip3 install --no-cache-dir flask

# install the scientific stuff here
RUN apk update &&\
    apk --no-cache add build-base gcc gfortran curl &&\
    apk --no-cache add openblas-dev

RUN pip3 install --no-cache-dir numpy==1.17.3 &&\
    pip3 install --no-cache-dir cython==0.29.13 &&\
    pip3 install --no-cache-dir joblib==0.14.0 &&\
    pip3 install --no-cache-dir pandas==0.25.2 &&\
    pip3 install --no-cache-dir scipy==1.3.1 &&\
    pip3 install --no-cache-dir scikit-learn==0.21.3 &&\
    pip3 install --no-cache-dir nltk==3.4.0 &&\
    pip3 install --no-cache-dir spacy==2.1.8

# replace the uwsgi plugin for Python 3.7
RUN apk --no-cache add linux-headers pcre-dev &&\
    pip3 install --no-cache-dir uwsgi==2.0.18 &&\
    cp /usr/local/bin/uwsgi /usr/sbin/uwsgi

# install language dictionaries needed by NLP libraries
RUN /usr/local/bin/python -m spacy download xx &&\
    /usr/local/bin/python -m spacy download en &&\
    /usr/local/bin/python -m nltk.downloader stopwords &&\
    /usr/local/bin/python -m nltk.downloader stopwords &&\
    /usr/local/bin/python -m nltk.downloader wordnet &&\
    /usr/local/bin/python -m nltk.downloader omw &&\
    /usr/local/bin/python -m nltk.downloader punkt &&\
    /usr/local/bin/python -m nltk.downloader averaged_perceptron_tagger

# replace the supervisord configuration in order to use the proper PYTHONPATH
COPY ./uwsgi_flask_nginx/supervisord/supervisord.ini /etc/supervisor.d/

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
# ENV NGINX_MAX_UPLOAD 1m
ENV NGINX_MAX_UPLOAD 0

# By default, Nginx listens on port 80.
# To modify this, change LISTEN_PORT environment variable.
# (in a Dockerfile or with an option for `docker run`)
ENV LISTEN_PORT 80

# Which uWSGI .ini file should be used, to make it customizable
ENV UWSGI_INI /app/uwsgi.ini

# URL under which static (not modified by Python) files will be requested
# They will be served by Nginx directly, without being handled by uWSGI
ENV STATIC_URL /static
# Absolute path in where the static files wil be
ENV STATIC_PATH /app/static

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
# ENV STATIC_INDEX 1
ENV STATIC_INDEX 0

# Add demo app
COPY ./app /app
WORKDIR /app

# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.
ENV PYTHONPATH=/app

# Copy start.sh script that will check for a /app/prestart.sh script and run it before starting the app
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Copy the entrypoint that will generate Nginx additional configs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
CMD ["/start.sh"]
