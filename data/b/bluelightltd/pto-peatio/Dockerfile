FROM bluelightltd/peatio

USER root
RUN mkdir -p /opt/peatio/config/ && \
    mkdir -p /home/app/ 

COPY seed  /opt/peatio/config/seed
COPY management_api_v1.yml   /opt/peatio/config/management_api_v1.yml
COPY plugins.yml   /opt/peatio/config/plugins.yml


