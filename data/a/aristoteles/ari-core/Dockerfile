FROM jboss/wildfly:14.0.1.Final

USER root

RUN yum reinstall -q -y glibc-common
RUN cp /usr/share/i18n/locales/pt_BR pt_BR_abnt\.src
RUN mkdir /usr/lib/locale/pt_BR_utf8_abnt

RUN localedef -i pt_BR -f ISO-8859-1 pt_BR.ISO-8859-1
RUN localedef -i pt_BR -f UTF-8 pt_BR.UTF-8

ENV LANG pt_BR.UTF-8 
ENV LANGUAGE pt_BR:en 
ENV LC_ALL pt_BR.UTF-8

ENV SYSTEM_ENVIRONMENT "production"
ENV SYSTEM_UPDATE_DATABASE_FIELDS "false"
ENV SYSTEM_UPDATE_DATABASE_EXECUTE_SCRIPT "false"
ENV SYSTEM_UPDATE_DATABASE_PATH_SCRIPT "/opt/jboss/wildfly/resources/data.sql"
ENV SYSTEM_LOGGER_DATA "false"
ENV HIBERNATE_DEFAULT_CATALOG "sgai"
ENV HIBERNATE_HBM2DDL_AUTO "none"
ENV HIBERNATE_SHOW_SQL "false"
ENV HIBERNATE_FORMAT_SQL "false"
ENV HIBERNATE_CACHE_USE_QUERY_CACHE "true"
ENV HIBERNATE_CACHE_USE_SECOND_LEVEL_CACHE "true"
ENV JPA_SHARED_CACHE_MODE ENABLED "ENABLED"
ENV JPA_NON_JTA_DATA_SOURCE "sgai"
ENV LOGIN_FAKE_INSTITUTION_CODE ""
ENV LOGIN_FAKE_USER ""
ENV LOGIN_FAKE_PASSWORD "" 
ENV REPORT_PATH "/opt/jboss/wildfly/resources/report/"
ENV REPORT_MAX_RESULT "50"
ENV JSF_TERM_CONTROL_COMPLETE_FORCE_SELECTION "false"
ENV FACES_STATE_SAVING_METHOD "server"
ENV FACELETS_DEVELOPMENT "false"
ENV FACELETS_REFRESH_PERIOD -1
#ENV WEB_XML_JAVAX_FACES_PROJECT_STAGE "Production"
ENV ARI_TRANSCRIPTION_API_PATH ""

ENV DATABASE_HOST "mysql"
ENV DATABASE_PORT "3306"
ENV DATABASE_SCHEMA "sgai"
ENV DATABASE_USER "user"
ENV DATABASE_PASS "pass"
ENV DATABASE_POOL_MIN 2
ENV DATABASE_POOL_MAX 20

ENV USER "user"
ENV PASSWD "passwd"

ADD wildfly/mysql /opt/jboss/wildfly/modules/system/layers/base/com/mysql
 
ADD sga-ear/target/sga-ear.ear /opt/jboss/wildfly/standalone/deployments/

ADD wildfly/database /opt/jboss/wildfly/resources/database

ADD wildfly/report /opt/jboss/wildfly/resources/report

ADD wildfly/config/standalone.xml /opt/jboss/wildfly/standalone/configuration/standalone.xml

ADD wildfly/config/application-roles.properties /opt/jboss/wildfly/standalone/configuration/application-roles.properties

ADD wildfly/config/application-users.properties /opt/jboss/wildfly/standalone/configuration/application-users.properties

ADD wildfly/welcome-content /opt/jboss/wildfly/welcome-content

RUN /opt/jboss/wildfly/bin/add-user.sh ${USER} ${PASSWD} --silent

VOLUME sga-wildfly-deployments /opt/jboss/wildfly/standalone/deployments/

#CMD ["rm -R /opt/jboss/wildfly/standalone/tmp/*"]

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]