FROM jboss/wildfly:10.0.0.Final
ENV ADM_PWD=s3cr3t
RUN /opt/jboss/wildfly/bin/add-user.sh admin $ADM_PWD --silent
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]

