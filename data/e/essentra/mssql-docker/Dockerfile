# use MSSQL 2017 image on Ubuntu 16.04
FROM microsoft/mssql-server-linux:2017-latest

# create directory within SQL container for database files
RUN mkdir -p /opt/mssql-scripts

# copy the database files from host to container
COPY sql/000_create_db.sql /opt/mssql-scripts

# set environment variables
ENV MSSQL_SA_PASSWORD=1qaz@WSX3edc
ENV ACCEPT_EULA=Y

# run initial scripts
#RUN /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'P@ssw0rd' -i /opt/mssql-scripts/000_create_db.sql
RUN /opt/mssql/bin/sqlservr --accept-eula & sleep 30 \
    && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '1qaz@WSX3edc' -i /opt/mssql-scripts/000_create_db.sql \
    && pkill sqlservr