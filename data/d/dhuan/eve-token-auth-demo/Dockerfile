FROM tiangolo/uwsgi-nginx-flask:python3.7

LABEL maintainer="Huan Di <hd@iamhd.top>" \
      description="This image is used as a eve token auth demo." \
      version="0.0.1"

# Add app
RUN rm /app/*
COPY ./app /app/app
# VOLUME ["/app/dmicros"]
WORKDIR /app/

ENV UWSGI_INI=/app/app/uwsgi.ini
# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.
ENV PYTHONPATH=/app

# set env
# db path
ENV MONGO_URI 'mongodb://mongo:27017/test'
ENV DEBUG 'False'
ENV TOKEN_AUTHOR '171b54871ecf1a08'
# support for host:post turned off
# set site envs, use `EVE_` prefix to avoid conflicts
# CORS

# ENV EVE_X_DOMAINS '*'
# ENV EVE_X_HEADERS 'Authorization,Content-Type'
# resource methods
# ENV EVE_RESOURCE_METHODS 'GET,POST,DELETE'
# ENV EVE_ITEM_METHODS 'GET,PATCH,PUT,DELETE'

# Do install
COPY pip.conf /etc/pip.conf
COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock
COPY init.py ./init.py

RUN pip install --upgrade pip && pip install pipenv \
    && pipenv install -d \
    && pipenv install --system \
    && pipenv --rm \
    && pip uninstall -y pipenv

WORKDIR /app/app
# DO_INIT -> reset database and add a default token author see init.py
ENV DO_INIT 'True'
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]
