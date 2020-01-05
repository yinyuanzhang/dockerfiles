FROM eikek/ox-common
#RUN apt-get update && apt-get -y install open-xchange open-xchange-authentication-database open-xchange-grizzly \
#  open-xchange-admin open-xchange-appsuite \
#  open-xchange-appsuite-backend open-xchange-appsuite-manifest \
#  open-xchange-meta-singleserver \
# && apt-get clean

WORKDIR /opt/open-xchange

#Patch the open-xchange start script not to redirect output streams to a file
RUN cp sbin/open-xchange /tmp/open-xchange.old
RUN sed 's/>> $CONSOLELOG 2>&1//' /tmp/open-xchange.old > sbin/open-xchange

#Use logging config, which logs to stdout
ADD logback.xml etc/logback.xml

#Rename the etc folder, containers will mount volumes in the etc folder, so we make a backup which we
#use to initialize the new empty volumes on initial startup
RUN mv etc etc_template

EXPOSE 9999
EXPOSE 8009

#Add scripts
WORKDIR /opt/open-xchange/sbin
ADD dockerox ./
RUN chmod a+x dockerox

VOLUME ["/opt/open-xchange/etc", "/var/opt/filestore"]

CMD /opt/open-xchange/sbin/dockerox

#CMD "/bin/bash"
