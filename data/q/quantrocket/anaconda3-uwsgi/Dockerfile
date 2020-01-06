FROM continuumio/anaconda3:5.2.0

MAINTAINER QuantRocket <support@quantrocket.com>

# N.B: Don't call this UWSGI_VERSION: https://github.com/unbit/uwsgi/issues/898
# However, we do set UWSGI_WORKERS and UWSGI_THREADS here
ENV UWSGIVERSION=2.0.18 \
  HOUSTON_URL=http://houston \
  IBAPI_VERSION=9.73.07.4 \
  UWSGI_WORKERS=1 \
  UWSGI_THREADS=2 \
  SQLITE3_VERSION=3270200 \
  PYTHON_VERSION=3.6.6

# Anaconda 5+ provides its own compilers instead of using the system ones;
# Conda packages for building uwsgi are copied from
# https://github.com/conda-forge/uwsgi-feedstock/tree/master/recipe
# (some might not be necessary)
RUN conda install -c https://metachannel.conda-forge.org/anaconda,conda-forge/gcc_linux-64,gxx_linux-64,python,jansson,libxml2,openssl,pcre,yaml,zlib,icu,pytables,pandas,keras,joblib,tensorflow,psycopg2 \
    gcc_linux-64 \
    gxx_linux-64 \
    python=${PYTHON_VERSION} \
    jansson \
    libxml2 \
    openssl \
    pcre \
    yaml \
    zlib \
    # fix broken lxml (used by master), see https://github.com/greenelab/snorkeling/issues/19#issuecomment-313200208
    # try to remove in future
    icu=58 \
    # fix broken pytables/h5py (used in zipline), must also specify numpy version
    # or 2 versions end up getting installed; try to remove in future
    pytables \
    h5py \
    numpy=1.14.3 \
    # Update pandas (Anaconda 5.2.0 ships with pandas 0.23.0 which has regressions)
    pandas=0.23.4 \
    # Add ML packages
    keras=2.2.4 \
    joblib=0.13.2 \
    tensorflow=1.12.0 \
    # Add PostgreSQL python client
    psycopg2

# install uWSGI (libssl-dev is required by uWSGI websockets)
RUN apt-get update && apt-get install -y \
  libssl-dev \
  unzip \
  && curl --fail --output /tmp/uwsgi.zip https://codeload.github.com/unbit/uwsgi/zip/${UWSGIVERSION} \
  && cd /tmp \
  && unzip uwsgi.zip \
  && mv uwsgi-${UWSGIVERSION} uwsgi \
  && rm uwsgi.zip

# We need sqlite3 3.20.0+ to allow the DATE function in indexes
# https://sqlite.org/deterministic.html#special_case_processing_for_date_time_functions
# Also, --enable-readline to support command history, and increase
# max variables from default 999 to 12000
RUN curl --fail --output /tmp/sqlite3.tar.gz "https://www.sqlite.org/2019/sqlite-autoconf-${SQLITE3_VERSION}.tar.gz" \
&& cd /tmp \
&& tar xvfz sqlite3.tar.gz \
&& cd sqlite-autoconf-${SQLITE3_VERSION} \
&& apt-get update && apt-get install -y \
  build-essential \
  libreadline-dev \
&& ./configure --prefix=/opt/conda --enable-readline \
&& echo 'DEFS += -DSQLITE_MAX_VARIABLE_NUMBER=12000' >> Makefile \
&& make \
&& make install \
&& cd / \
&& rm -r /tmp/sqlite-autoconf-* \
&& rm /tmp/sqlite3.tar.gz \
&& apt-get remove -y \
  build-essential \
  libreadline-dev

## Add psql client
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >> /etc/apt/sources.list.d/pgdg.list \
  && wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && apt-get update \
  && apt-get install -y postgresql-client-11

# Install ibapi
 RUN curl --fail --output /tmp/ibapi.zip https://codeload.github.com/quantrocket-llc/ibapi/zip/${IBAPI_VERSION} \
   && cd /tmp \
   && unzip ibapi.zip \
   && cd ibapi-${IBAPI_VERSION}/source/pythonclient \
   && pip install . \
   && apt-get remove -y unzip \
   && cd /tmp \
   && rm -r ibapi-${IBAPI_VERSION} \
   && rm ibapi.zip

EXPOSE 80

# Install pip packages
RUN /bin/bash -c "source activate base" \
  && pip install \
  # Flask et al
  flask==0.12 \
  dnspython==1.15.0 \
  uwsgi-tools==1.0.3 \
  flask-restful==0.3.5 \
  webargs==1.6.0 \
  Werkzeug==0.12.2 \
  marshmallow==2.19.5 \
  # utils/ib/quantrocket clients
  csvkit==1.0.3 \
  ibpythonic==0.1.5 \
  quantrocket-client \
  ib-trading-calendars \
  # ML package
  xgboost==0.82 \
  && /bin/bash -c "source deactivate"

COPY uwsgi /etc/uwsgi
COPY build.ini /tmp/uwsgi/buildconf/quantrocket.ini
COPY build_dev.ini /tmp/uwsgi/buildconf/quantrocket_dev.ini
COPY qrocket /tmp/uwsgi/qrocket
COPY qrocket/servicename.py /opt/conda/bin/servicename
COPY build*.sh /tmp/

RUN chmod +x /tmp/build*.sh \
 && chmod +x /opt/conda/bin/servicename \
 && mkdir -p /var/tmp/uwsgi/spool

ONBUILD CMD ["uwsgi-quantrocket", "--ini", "/etc/uwsgi/uwsgi.ini"]
