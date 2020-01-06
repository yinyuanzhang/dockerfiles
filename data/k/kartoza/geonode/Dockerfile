FROM python:2.7.14-stretch
MAINTAINER GeoNode development team

RUN mkdir -p /usr/src/{app,geonode}

WORKDIR /usr/src/app

# This section is borrowed from the official Django image but adds GDAL and others
RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		postgresql-client libpq-dev \
		sqlite3 \
                python-gdal python-psycopg2 \
                python-imaging python-lxml \
                python-dev libgdal-dev \
                python-ldap \
                libmemcached-dev libsasl2-dev zlib1g-dev \
                python-pylibmc \
                uwsgi uwsgi-plugin-python \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*


COPY wait-for-databases.sh /usr/bin/wait-for-databases
RUN chmod +x /usr/bin/wait-for-databases

# Upgrade pip
RUN pip install --upgrade pip

# To understand the next section (the need for requirements.txt and setup.py)
# Please read: https://packaging.python.org/requirements/

# python-gdal needs to be reinstalled, because we are not using python from debian distribution
# python-gdal uses GDAL 2.1.2 but there are no python package for that, so we are using 2.1.0
RUN pip install GDAL==2.1.0 --global-option=build_ext --global-option="-I/usr/include/gdal"

# install shallow clone of geonode master branch
ARG GEONODE_BRANCH=master
RUN git clone --depth=1 git://github.com/GeoNode/geonode.git --branch ${GEONODE_BRANCH} /usr/src/geonode
RUN cd /usr/src/geonode/; pip install --upgrade --no-cache-dir -r requirements.txt; pip install --upgrade -e .


RUN cp /usr/src/geonode/tasks.py /usr/src/app/
RUN cp /usr/src/geonode/entrypoint.sh /usr/src/app/

RUN chmod +x /usr/src/app/tasks.py \
    && chmod +x /usr/src/app/entrypoint.sh


# use latest master
ONBUILD RUN cd /usr/src/geonode/; git pull ; pip install --upgrade --no-cache-dir -r requirements.txt; pip install --upgrade -e .
ONBUILD COPY . /usr/src/app
ONBUILD RUN pip install --upgrade --no-cache-dir -r /usr/src/app/requirements.txt
ONBUILD RUN pip install -e /usr/src/app --upgrade

# Update the requirements from the local env in case they differ from the pre-built ones.
ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --upgrade --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app/
ONBUILD RUN pip install --upgrade --no-cache-dir -e /usr/src/app/

EXPOSE 8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["uwsgi", "--ini", "/usr/src/app/uwsgi.ini"]
