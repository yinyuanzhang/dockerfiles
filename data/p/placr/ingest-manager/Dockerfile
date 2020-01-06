FROM        	python:2.7
MAINTAINER  	Jan Verhoeven (jan@visity.nl)

# grab gosu for easy step-down from root
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -fSL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
	&& curl -o /usr/local/bin/gosu.asc -fSL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu
	
RUN 			apt-get update && \
				apt-get install -y --no-install-recommends postgresql-client-9.4 libpq-dev git nginx python-mediainfodll nano less && \
				rm -rf /var/lib/apt/lists/*

# Install feedparser from git repo
RUN 			pip install git+git://github.com/sklaus/feedparser.git@367c936b2b5421e9091bf2c730a93ca56cbd8783#egg=feedparser

ADD 			deploy/requirements.txt /tmp/pip/requirements.txt

WORKDIR 		/tmp/pip

RUN 			pip install -r requirements.txt

# User to run the django process
RUN      		addgroup --gid 30100 visity
RUN      		useradd -u 30101 -g visity -s /bin/false im

# for sftp testing
RUN 			mkdir  /etc/visity
ADD 			deploy/configfiles/sftp/sftp_key.conf /etc/visity/rsa_key_test
RUN 			chown im:visity /etc/visity/rsa_key_test
RUN 			chmod 600 /etc/visity/rsa_key_test

#add kd staging key
ADD 			deploy/configfiles/sftp/kd_staging_key.conf /etc/visity/rsa_key_staging
RUN 			chown im:visity /etc/visity/rsa_key_staging
RUN 			chmod 600 /etc/visity/rsa_key_staging
#add kd live key
ADD 			deploy/configfiles/sftp/kd_live_key.conf /etc/visity/rsa_key_live
RUN 			chown im:visity /etc/visity/rsa_key_live
RUN 			chmod 600 /etc/visity/rsa_key_live

# Some additional deploy scripts for starting when booting the machine.
RUN      		mkdir -p /opt/im/deploy_scripts
ADD      		deploy/deploy_scripts/ /opt/im/deploy_scripts/
RUN      		chmod u+x /opt/im/deploy_scripts/migrate-db.sh

# Create folder and set rights.
RUN             mkdir -p /var/log/visity && chown -R im:visity /var/log/visity
RUN 			mkdir  /im_extracttarget && chown -R im:visity /im_extracttarget
RUN 			mkdir  /im_messages && chown -R im:visity /im_messages

# Copy the application in
ADD 			src  /app
RUN             rm -f /app/MediaInfoDLL*.*
RUN      		chown -R im:visity /app

# collect the statics for the django project since we are now running with DEBUG=False in Django settings
RUN             export PYTHONPATH=/app/ && django-admin.py collectstatic --settings=ingestmanager.settings.deployment --noinput

# Install nginx config
ADD             deploy/nginx/django.conf /etc/nginx/sites-enabled/
RUN             rm /etc/nginx/sites-enabled/default
ADD			    deploy/nginx/nginx.conf /etc/nginx/nginx.conf

# Install fdtvg.com certificate or the RSS feeds will not be retrievable.
RUN             mkdir -p /usr/local/share/ca-certificates/fdtvg.com/
COPY            deploy/fdtvg.com/ /usr/local/share/ca-certificates/fdtvg.com/
RUN             update-ca-certificates

COPY            docker-entrypoint.sh /

# In case of using debian:jessie: Media info is installed in /usr/lib/python2.7/dist-packages and not: /usr/local/lib/python2.7/site-packages/
# so add it to the PYTHONPATH
ENV 			PYTHONPATH $PYTHONPATH:/app:/usr/lib/python2.7/dist-packages

WORKDIR 		/app

VOLUME         /var/log/visity
VOLUME         /im_messages
VOLUME         /im_extracttarget

EXPOSE 			8100

ENTRYPOINT      ["/docker-entrypoint.sh"]

CMD             ["django"]
