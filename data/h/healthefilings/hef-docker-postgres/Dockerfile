FROM postgres:9.5
MAINTAINER Oscar Rocha <orocha@healthefilings.com>

# Add debian stretch repository
RUN echo "deb http://ftp.us.debian.org/debian/ stretch main contrib non-free" >> /etc/apt/sources.list
# Fix locales
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf
RUN locale-gen en_US.UTF-8

# Install dependencies
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-setuptools \
    libffi-dev libsnappy-dev python3-all python3-cryptography python3-dateutil \
    python3-flake8 python3-psycopg2 python3-pytest python3-requests \
    python3-snappy pylint supervisor
RUN easy_install3 pip
RUN pip3 install boto pghoard==1.5 oauth2client==3.0.0 google-api-python-client

# Add configuration to PGDATA folder
COPY config/pg_hba.conf "/usr/share/postgresql/9.5/pg_hba.conf"
COPY config/postgresql.conf "/usr/share/postgresql/9.5/postgresql.conf"
COPY hef-config.sh /docker-entrypoint-initdb.d/hef-config.sh
# Add supervisor configuration file
ADD config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN chmod 755 /docker-entrypoint-initdb.d/hef-config.sh

CMD ["/usr/bin/supervisord"]

EXPOSE 5432
