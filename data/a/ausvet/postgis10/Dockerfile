FROM ubuntu:16.04

# Set the locale
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_AU.UTF-8
# RUN timedatectl set-timezone Australia/Perth

RUN dpkg-reconfigure locales && \
    localedef -i en_AU -c -f UTF-8 en_AU.UTF-8 && \
    export LANGUAGE="en_AU.UTF-8" && \
    export LANG="en_AU.UTF-8"

RUN apt-get update  && \
    apt-get install -y \
        software-properties-common \
        python-software-properties \
        wget

RUN apt-get install -y ntp && \
    echo "server 1.sg.pool.ntp.org" >> /etc/ntp.conf  && \
    echo "server 3.asia.pool.ntp.org" >> /etc/ntp.conf  && \
    echo "server 2.asia.pool.ntp.org" >> /etc/ntp.conf

RUN add-apt-repository -y "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - 

RUN add-apt-repository -y "deb http://cran.stat.nus.edu.sg/bin/linux/ubuntu xenial/" && \
     apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E084DAB9

RUN apt-get update -y && apt-get upgrade -y 

RUN apt-get install -y \
    postgresql-10-postgis-2.4 \
    postgresql-plpython-10 \
    postgresql-plpython3-10 \
    postgresql-contrib \
    r-base-dev \
    postgresql-10-plr \
    libpq-dev \
    postgresql-server-dev-10 \
    libcairo2-dev \
    libxt-dev \
    python-dev \
    python-pip \
    python3-dev \
    python3-pip


# RUN    add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable  && \
#     apt-get update  && \
#     apt-get install -y postgis  && \
#     # apt-get install -y postgis-gui  && \
#     apt-get install -y gdal-bin python3-gdal

# SETUP Python
RUN	apt-get install -y python3-pip  && \
    python3 -m pip install  && \
    python3 -m pip install --upgrade pip  && \
    python3 -m pip install pytest && \
    python3 -m pip install -U awscli boto boto3 botocore

RUN python -m pip install -U boto boto3 botocore

RUN	apt-get install -y python3-venv

# SETUP Python3
COPY ./pip3-requirements.txt /pip3-requirements.txt
RUN pip3 install -U -r pip3-requirements.txt
COPY ./isikhnas_db_functions.zip /isikhnas_db_functions.zip
RUN pip3 install -U /isikhnas_db_functions.zip

# SETUP R
COPY ./installpackages.r /installpackages.r
RUN Rscript /installpackages.r

ENV POSTGRES_PASSWORD password
ENV POSTGRES_USER postgres
ENV POSTGRES_DB ${POSTGRES_USER}
ENV PGDATA /var/lib/postgresql/data
ENV PG_LOG_FILE /var/log/postgresql/postgresql-10-main.log

RUN mkdir -p ${PGDATA} && \
    chown -R postgres:postgres ${PGDATA} && \
    chmod 777 ${PGDATA} # this 777 will be replaced by 700 at runtime (allows semi-arbitrary "--user" values)
VOLUME [${PGDATA}]

RUN echo ${PGDATA}

COPY ./postgis_entrypoint.sh /postgis_entrypoint.sh

# Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.3`` package when it was ``apt-get installed``
USER postgres

ENTRYPOINT ["/postgis_entrypoint.sh"]

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
# VOLUME  ["/etc/postgresql", "/var/log/postgresql", "$PGDATA"]

# Set the default command to run when starting the container
# CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", ${PGDATA}, "-c", "config_file=/etc/postgresql/10/main/postgresql.conf"]
# CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/10/main", "-c", "config_file=/etc/postgresql/10/main/postgresql.conf"]
# CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/data", "-c", "config_file=/etc/postgresql/10/main/postgresql.conf"]
CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/data"]
