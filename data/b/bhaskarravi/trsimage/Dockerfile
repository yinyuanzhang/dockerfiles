#Pull the relevant base image 
# for java 6 and tomcat 7 use bhaskarravi/imagefortrs:j6t7
# for java 7 and tomcat 7 use bhaskarravi/imagefortrs:j7t7
# for java 8 and tomcat 7 use bhaskarravi/imagefortrs:j8t7
# for latest version : tomcat 7 and java 8 use bhaskarravi/imagefortrs

#tomcat with catalogger
# Pull base image.
FROM dockerfile/ubuntu

#Proxy settings
#ENV http_proxy http://la-proxy.us.aegon.com:9090
#ENV https_proxy http://la-proxy.us.aegon.com:9090


# Install Java 7 .
RUN \
  apt-get update && \
  apt-get install -y openjdk-7-jdk && \
  rm -rf /var/lib/apt/lists/*

# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

# Define default command.
CMD ["bash"]


# Install tomcat 7
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH:$CATALINA_HOME/conf/cm

RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \
05AB33110949707C93A279E3D3EFE6B686867BA6 \
07E48665A34DCAFAE522E5E6266191C37C037D42 \
47309207D818FFD8DCD3F83F1931D684307A10A5 \
541FBE7D8F78B25E055DDEE13C370389288584E7 \
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \
713DA88BE50911535FE716F5208B0AB1D63011C7 \
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \
9BA44C2621385CB966EBA586F72C284D731FABEE \
A27677289986DB50844682F8ACB77FC2E86E29AC \
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23
ENV TOMCAT_MAJOR 7
ENV TOMCAT_VERSION 7.0.59
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz
RUN curl -SL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \
&& curl -SL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \
&& gpg --verify tomcat.tar.gz.asc \
&& tar -xvf tomcat.tar.gz --strip-components=1 \
&& rm bin/*.bat \
&& rm tomcat.tar.gz*




#my application
#RUN mkdir /usr/local/tomcat/webapps


#ADD CatalogManagement.war /usr/local/tomcat/webapps/CatalogManagement.war
#ADD tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml


#mkdir /usr/local/tomcat/conf/cm
#ADD config_dm/* /usr/local/tomcat/conf/cm/

#ENV CLASSPATH $CATALINA_HOME/conf/cm

EXPOSE 8080
#ENV JAVA_OPTS -Dserver.root=/usr/local/tomcat/conf/cm/ -Dconfig.bootstrap.location=config_env.properties 

#CMD ["catalina.sh", "run"] 
