FROM python:2.7.14
MAINTAINER SIMSAB

RUN mkdir -p /opt/{app,geonode}

WORKDIR /opt/app

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
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# To understand the next section (the need for requirements.txt and setup.py)
# Please read: https://packaging.python.org/requirements/

# python-gdal does not seem to work, let's install manually the version that is
# compatible with the provided libgdal-dev
RUN pip install GDAL==1.10 --global-option=build_ext --global-option="-I/usr/include/gdal"

# install shallow clone of geonode dev branch
RUN git clone --depth=1 git://github.com/simsab-ufcg/geonode.git --branch develop /opt/geonode
RUN cd /opt/geonode/; pip install --upgrade --no-cache-dir -r requirements.txt; pip install --upgrade -e .


RUN cp /opt/geonode/tasks.py /opt/app/
RUN cp /opt/geonode/entrypoint.sh /opt/app/

RUN chmod +x /opt/app/tasks.py \
    && chmod +x /opt/app/entrypoint.sh


# use latest master
ONBUILD RUN cd /opt/geonode/; git pull ; pip install --upgrade --no-cache-dir -r requirements.txt; pip install --upgrade -e .
ONBUILD COPY . /opt/app
ONBUILD RUN pip install --upgrade --no-cache-dir -r /opt/app/requirements.txt
ONBUILD RUN pip install -e /opt/app --upgrade

# Update the requirements from the local env in case they differ from the pre-built ones.
ONBUILD COPY requirements.txt /opt/app/
ONBUILD RUN pip install --upgrade --no-cache-dir -r requirements.txt

ONBUILD COPY . /opt/app/
ONBUILD RUN pip install --upgrade --no-cache-dir -e /opt/app/

EXPOSE 8000

ENTRYPOINT ["/opt/app/entrypoint.sh"]
CMD ["uwsgi", "--ini", "/opt/app/uwsgi.ini"]