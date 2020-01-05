FROM tomcat:8-jre8
MAINTAINER Michele Fenech Adami <michele@sapho.com>

ENV IMAGE_VERSION 5.4.1
ENV SAPHO_DB_HOSTNAME mysql
ENV SAPHO_DB_PASSWORD p244w0rd
ENV SAPHO_DB_PORT 3306
ENV SAPHO_DB_TYPE mysql
ENV SAPHO_DB_NAME sapho
ENV SAPHO_DB_USERNAME root
ENV SAPHO_MEMORY_LIMIT 2g
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
WORKDIR /root

COPY launch.sh ${CATALINA_HOME}/bin/

RUN apt-get update && \
    echo GMT > /etc/timezone && \
    chmod +x ${CATALINA_HOME}/bin/launch.sh && \
    apt-get install -y jq && \
    rm -rf /var/lib/apt/lists/*

RUN rm -rf /${CATALINA_HOME}/webapps/ROOT && rm -rf /${CATALINA_HOME}/webapps/docs
RUN rm -rf /${CATALINA_HOME}/webapps/examples && rm -rf /${CATALINA_HOME}/webapps/host-manager
RUN rm -rf /${CATALINA_HOME}/webapps/manager  

#RUN wget -q -O sapho-latest.zip https://s3-us-west-1.amazonaws.com/download.sapho.com/sapho-$IMAGE_VERSION.zip

CMD ["launch.sh"]