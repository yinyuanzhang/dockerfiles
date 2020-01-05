FROM python:2.7.7

ENV DEBIAN_FRONTEND         noninteractive

ENV PYTHONUNBUFFERED        1
ENV PYTHONPATH              /code:/usr/local/lib/python2.7/site-packages
ENV UWSGI_CALLABLE          app
ENV UWSGI_PYTHON_AUTORELOAD 1
#ENV UWSGI_PY_TRACEBACKER

ENV UWSGI_MASTER            true
ENV UWSGI_MASTER_AS_ROOT    true
ENV UWSGI_UID               app
ENV UWSGI_GID               app
ENV UWSGI_UWSGI_SOCKET      0.0.0.0:5000
ENV UWSGI_NO_ORPHANS        true
ENV UWSGI_VACUUM            true
ENV UWSGI_LOG_DATE          true

ENV UWSGI_LAZY_APPS         false
ENV UWSGI_WORKERS           2
ENV UWSGI_THREADS           1
ENV UWSGI_ENABLE_THREADS    true
ENV UWSGI_BUFFER_SIZE       65536
ENV UWSGI_MAX_REQUESTS      128
ENV UWSGI_HARAKIRI          120
ENV UWSGI_HARAKIRI_VERBOSE  true
ENV UWSGI_THUNDER_LOCK      true

ENV PGDATABASE              app
ENV PGUSER                  app
ENV PGPASSWORD              app
ENV PGHOST                  db
ENV PGPORT                  5432

RUN groupadd -r app && \
    useradd -r -g app -d /code app

RUN apt update && \
    apt install -y \
      build-essential \
      python-dev \
      python-setuptools && \
    rm -rf /var/lib/apt/lists/*
RUN pip install \
      'uWSGI >=2.0, <2.1'

EXPOSE 5000
CMD ["uwsgi"]
