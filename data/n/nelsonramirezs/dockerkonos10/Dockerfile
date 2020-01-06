FROM nelsonramirezs/odoo10:latest
MAINTAINER Nelson Ramirez <info@konos.cl>


USER root


ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && apt-get install -y locales -qq
RUN echo 'es_CL.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
RUN echo 'es_US.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
RUN echo 'C.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
RUN dpkg-reconfigure locales && /usr/sbin/update-locale LANG=C.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# sudo and other useful tools
RUN apt-get install -y sudo nano htop ssh wget unzip iputils-ping telnet

# Let's hack around setting up ssh key to clone a private github repo.
RUN mkdir /root/.ssh/
ADD id_rsa /root/.ssh/id_rsa
RUN chmod 600 -R /root/.ssh
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts

# we update postgres-client to 9.6 because we use 9.6 postgres and if not database backup wont work, we need wget to run this
#RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" > /etc/apt/sources.list.d/pgdg.list
#RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
#RUN apt-get update && apt-get install -y postgresql-client-9.6  python-pip git vim


RUN apt-get install -y ghostscript  && \
    apt-get install -y python-gevent  && \
    apt-get install -y python-dev freetds-dev  build-essential && \
    apt-get install -y python-matplotlib font-manager  && \
    apt-get install -y swig libffi-dev libssl-dev python-httplib2 mercurial  && \
    apt-get install -y libxml2-dev libxmlsec1-dev libxslt-dev python-dev lib32z1-dev liblz-dev
    
RUN apt-get install -y swig libssl-dev  && \
    apt-get install -y libcups2-dev && \
    apt-get install -y libxslt1-dev  python-lxml libxmlsec1-openssl python-openssl python-defusedxml
    
RUN apt-get install -y openssl && \
    apt-get install -y python-sqlalchemy && \
    apt-get install -y unixodbc-dev unixodbc-bin unixodbc

    
RUN apt-get -q update && apt-get -yq install --no-install-recommends gis-devel \
			python-scipy \
			python-matplotlib \
			python-shapely   
    

    
RUN pip install --upgrade pip 
RUN pip install certifi
#RUN pip install xmlsec


# Lets Encrypt
RUN pip install acme-tiny
RUN pip install IPy

# dte implementation
RUN pip install xmltodict
RUN pip install dicttoxml
RUN pip install elaphe
RUN pip install pdf417gen
#RUN pip install hashlib
RUN pip install cchardet
RUN pip install suds
RUN pip install urllib3
RUN pip install SOAPpy
RUN pip install cryptography
RUN pip install M2Crypto
RUN pip install --upgrade setupext-pip
RUN pip install signxml==1.0.1
#RUN pip install textwrap
#RUN pip install cStringIO
RUN pip install pysftp==0.2.8
RUN pip install urllib3==1.7.1
RUN pip install requests==2.6.0
RUN pip install xlsxwriter
RUN pip install dropbox
RUN pip install xlrd
RUN pip install validate_email
RUN pip install pytemperature

# Odoo 10 Other Version
RUN pip install --upgrade pip
RUN pip install ofxparse
RUN pip install pyserial
RUN pip install python-chart
RUN pip install pyusb>=1.0.0b1
RUN pip install suds-jurko
RUN pip install cryptography==1.8
RUN pip install openpyxl
RUN pip install paramiko
RUN pip install Crypto
RUN pip install signxml==2.5.2

# oca reports
RUN pip install xlwt


# PERU
RUN apt-get update && apt-get install -y libssl-dev pkg-config
RUN pip install xmlsec
RUN pip install BeautifulSoup4
RUN pip install pysimplesoap
RUN pip install pytesseract
RUN pip install qrcode

# create directories for repos
RUN mkdir -p /opt/odoo/stable-addons/oca
RUN mkdir -p /opt/odoo/.filelocal/odoo
RUN mkdir -p /var/lib/odoo/backups/synced


# update openerp-server.conf file (todo: edit with "sed")
COPY ./odoo.conf /etc/odoo/
RUN chown odoo /etc/odoo/odoo.conf
RUN chmod 644 /etc/odoo/odoo.conf
RUN chown -R odoo /opt/odoo
RUN chown -R odoo /opt/odoo/stable-addons
RUN chown -R odoo /mnt/extra-addons
RUN chown -R odoo /var/lib/odoo
# RUN chown -R odoo /mnt/filelocal/odoo

# oca partner contacts
RUN pip install unicodecsv

# aeroo direct print
RUN pip install pycups==1.9.68


RUN pip install xlsxwriter
RUN pip install setuptools --upgrade




RUN chown -R odoo:odoo /opt/odoo/stable-addons
 ##   WORKDIR /opt/odoo/stable-addons/
RUN chmod -R 755 /opt/odoo/stable-addons
WORKDIR /opt/odoo/stable-addons/


## Clean apt-get (copied from odoo)
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Change default aeroo host name to match docker name
##RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/docs_client_lib.py
##RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/installer.py
##RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/report_aeroo.py

# Set default user when running the container
USER odoo
