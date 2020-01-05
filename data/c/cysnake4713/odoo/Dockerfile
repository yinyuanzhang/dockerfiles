# DOCKER-VERSION 0.12.0
FROM cysnake4713/odoo8-base

#-----add code and install ------------------------
COPY . /opt/odoo/

RUN apt-get install -y libjpeg-dev python-dev
RUN wget http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz
RUN tar xvfz Imaging-1.1.7.tar.gz
RUN cd Imaging-1.1.7
RUN python Imaging-1.1.7/setup.py install
RUN apt-get install libjpeg-dev zlib1g-dev
RUN pip install -e /opt/odoo
#-------------------TODO:----------------------------------------
#RUN wget -nv -O /opt/temp.zip https://github.com/cysnake4713/odoo/archive/9.0.docker.zip
#-----------------------------------------------------------
#RUN unzip -q /opt/temp.zip -d /opt && mv /opt/odoo-9.0.docker /opt/odoo && rm /opt/temp.zip
#-----------------------------------------------------------

#-----------------------------------------------------------

RUN adduser --system --uid=1000 --home /home/odoo --shell /bin/bash odoo

# Declare volumes for data
VOLUME ["/home/odoo"]

# Expose HTTP port, and longpolling port
EXPOSE 8069 8072

#RUN chown -R odoo /var/lib/odoo 
ENV HOME $ODOO_HOME

USER odoo

CMD /opt/odoo/openerp-server -c /home/odoo/odoo.conf

