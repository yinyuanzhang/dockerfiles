from debian 
run apt-get update && \
    apt-get install -y maven openjdk-7-jdk && \
    apt-get clean 
add pom.xml /srv/testnul/
workdir /srv/testnul/
run mvn install
add src /srv/testnul/src/
expose 8080
cmd mvn jetty:run
