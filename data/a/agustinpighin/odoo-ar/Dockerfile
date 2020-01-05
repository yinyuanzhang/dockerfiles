FROM agustinpighin/odoo-oca:9.0
#MAINTAINER Agustin Pighin <agustinpighin@gmail.com>
LABEL maintainer="agustinpighin@gmail.com"

USER root

# Get repositories & add files
WORKDIR ${RESOURCES}
COPY ./adhoc-sources.txt ./
RUN mkdir -p ${EXTRA_ADDONS}
RUN python get_addons.py ${EXTRA_ADDONS} --depth=1 --sources_file=adhoc-sources.txt
WORKDIR /

ENV VAR_FOLDER /var
ENV BACKUP /var/odoo/backups/syncked
WORKDIR ${VAR_FOLDER}
RUN mkdir -p ${BACKUP}
RUN chmod 777 -R /var/odoo
WORKDIR /

# para pyafipws
RUN chmod 777 -R /usr/local/lib/python2.7/dist-packages/pyafipws/
# PATCH use_sslv3 to fix requests to padron arba
RUN sed  -i  "s/USE_SSLv3 = None/USE_SSLv3 = False/" /usr/local/lib/python2.7/dist-packages/pysimplesoap/transport.py

# seteamos SERVER_WIDE_MODULES de los modulos incluidos
ENV SERVER_WIDE_MODULES web,server_mode,database_tools,

USER odoo
