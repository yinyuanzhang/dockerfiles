FROM glassfish/server
ADD ReportServer-ear-1.1-SNAPSHOT.ear /glassfish4/
   
   
ADD execute.sh /glassfish4/glassfish/bin/
Run chmod 777 /glassfish4/glassfish/bin/execute.sh
# Ports being exposed
EXPOSE 4848 8080 8181 7676
CMD ["/glassfish4/glassfish/bin/execute.sh"]





