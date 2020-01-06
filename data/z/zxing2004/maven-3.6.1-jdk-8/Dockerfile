FROM maven:3.6.1-jdk-8
COPY settings.xml /usr/share/maven/conf/settings.xml
ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]
CMD ["mvn"]
