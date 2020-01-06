FROM softwareplant/oracle:clean

USER root

COPY jira7.dmp /home/oracle/jira7.dmp
COPY 03_restore_jira7.sh /docker-entrypoint-initdb.d/setup/03_restore_jira7.sh

RUN chmod 754 /home/oracle/jira7.dmp
RUN chmod 754 /docker-entrypoint-initdb.d/setup/03_restore_jira7.sh

RUN chown oracle:dba /home/oracle/jira7.dmp
RUN chown oracle:dba /docker-entrypoint-initdb.d/setup/03_restore_jira7.sh

USER oracle

RUN echo "oracle"

