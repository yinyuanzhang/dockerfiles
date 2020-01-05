FROM python:3.6.3-slim-jessie

# Oracle Instant Client layer
COPY instantclient/* /tmp/
# Apt China mirror
# COPY sources.list.jessie /etc/apt/sources.list

# fix pymssql error: sqlfront.h: No such file or directory
ENV PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1

RUN apt-get update && apt-get install -y alien libaio1 && \
    alien -iv /tmp/oracle-instantclient12.2-basiclite-12.2.0.1.0-1.x86_64.rpm && \
    alien -iv /tmp/oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm && \
    pip install --no-cache-dir cx_Oracle PyMySQL pymssql && \
    apt-get purge -y alien perl perl5 && apt-get -y autoremove && apt-get clean && \
    rm -rf /tmp/oracle-* && rm -rf /usr/share/docs && rm -rf /usr/share/man

# Environment variables
ENV ORACLE_HOME=/usr/lib/oracle/12.2/client64
ENV LD_LIBRARY_PATH=$ORACLE_HOME/lib
ENV PATH=$ORACLE_HOME/bin:$PATH

# Test cx_Oracle connection
# COPY test_conn.py /app/
# RUN python /app/test_conn.py

CMD ["pip", "list"]