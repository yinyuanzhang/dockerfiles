FROM ibadrtdinov/tomcat_https
ENV PORTAL_DB="10.36.6.50/sv"
ENV JENKINS_ARTIFACT_URL="http://10.36.6.49:9090/view/Trunk/job/portal_trunk/lastSuccessfulBuild/artifact/portal/dist/employee-portal.war"
ENV BLOCK_EM7="false"
ENV OPEN_AM="false" 
ENV OPENAM_HOME_URL="http://dev-test-ldap01-qts.carpathia.com:1288/openam/"
ADD configure_portal.sh ${CATALINA_HOME}/bin/
RUN sed -i '/#placeholder#/r bin/configure_portal.sh' ${CATALINA_HOME}/bin/entrypoint.sh
