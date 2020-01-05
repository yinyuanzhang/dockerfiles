# base this image of the SQL 2017 latest image
FROM microsoft/mssql-server-linux:latest
 
# make a directory within the container
RUN mkdir /var/opt/sqlserver
 
# copy attach-db.sh into container
COPY restore-db.sh /var/opt/sqlserver

# USE ADD 
ADD https://github.com/aleta-systems/aletasystems.role.data.engineer.phase1/raw/master/database/WideWorldImporters-Full.bak /var/opt/sqlserver/

# set script executable
RUN ["chmod", "+x", "/var/opt/sqlserver/restore-db.sh"]

# use the ENTRYPOINT command to execute the script and start SQL Server
ENTRYPOINT /var/opt/sqlserver/restore-db.sh & /opt/mssql/bin/sqlservr