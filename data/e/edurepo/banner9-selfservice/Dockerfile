# SSL keystore generation
FROM alpine:latest as TLS

# Add openssl CLI
RUN apk add --no-cache openssl

WORKDIR /tls
RUN openssl req -newkey rsa:2048 -new -nodes -keyout key.pem -out csr.pem -subj '/CN=localhost'
RUN openssl x509 -req -days 36500 -in csr.pem -signkey key.pem -out server.crt

FROM oraclelinux:7 as java8

RUN yum install gzip tar curl -y && rm -rf /var/cache/yum

ENV JAVA_VERSION=8u181 \
    JAVA_BNUMBER=13 \
    JAVA_SEMVER=1.8.0_181 \
    JAVA_HOME=/opt/jre-home \
    JAVA_HASH=96a7b8442fe848ef90c96a2fad6ed6d1 \
    TIMEZONE=America/New_York


ENV PATH=$PATH:$JAVA_HOME/bin
RUN cd / \
    && curl --header "Cookie: oraclelicense=accept-securebackup-cookie" -fSL \
    http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-b$JAVA_BNUMBER/$JAVA_HASH/server-jre-$JAVA_VERSION-linux-x64.tar.gz \
    -o server-jre-$JAVA_VERSION-linux-x64.tar.gz \
    && tar -zxvf server-jre-$JAVA_VERSION-linux-x64.tar.gz -C /opt \
    && rm server-jre-$JAVA_VERSION-linux-x64.tar.gz \
    && ln -s /opt/jdk$JAVA_SEMVER/ /opt/jre-home;

FROM java8 as tomcat8

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN groupadd -r tomcat && useradd -r -g tomcat tomcat
RUN mkdir -p "$CATALINA_HOME" && chown tomcat:tomcat "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS
RUN  for key in \
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
		F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23 \
	; do \
		gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	done

ENV TOMCAT_MAJOR=8
ENV TOMCAT_VERSION=8.0.53
ENV TOMCAT_TGZ_URL=https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz


RUN set -x \
  && curl -fSL $TOMCAT_TGZ_URL -o tomcat.tar.gz \
	&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \
	&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
	&& rm bin/*.bat \
	&& rm tomcat.tar.gz* \
  && rm -rf webapps/* \
  && chown -R tomcat:tomcat $CATALINA_HOME

FROM tomcat8 as tomcat8-native-build

# Tomcat native - dependencies
RUN yum install \
    gcc \
    apr \
    apr-devel \
    openssl \
    openssl-devel \
    -y && rm -rf /var/cache/yum
# let Tomcat Native live somewhere isolated
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR
# Build Tomcat Native
RUN tar -zxf bin/tomcat-native.tar.gz \
 && cd tomcat-native-*/native \
 && ./configure --with-apr=/usr/bin/apr-1-config \
            --with-ssl=yes \
            --with-java-home=$JAVA_HOME \
            --prefix=$PWD \
 && make \
 && make install \
 && mv lib $CATALINA_HOME/native-jni-lib \
 && cd $CATALINA_HOME \
 && rm -rf tomcat-native-*/

FROM tomcat8-native-build as banner9-selfservice

ENV XMS=2g XMX=8g BANNERDB_JDBC=jdbc:oracle:thin:@//oracle.example.edu:1521/prod \
  DEFAULT_ROW_PREFETCH=10 \
  REMOVE_ABANDONED_ON_MAINTENANCE=true \
  REMOVE_ABANDONED_ON_BORROW=true \
  REMOVE_ABANDONED_TIMEOUT=300 \
  LOG_ABANDONED=false \
  MAX_THREADS=500 \
  MIN_SPARE_THREADS=25 \
  BANPROXY_USERNAME=banproxy \
  BANPROXY_INITALSIZE=25 \
  BANPROXY_MAXTOTAL=600 \
  BANPROXY_MAXIDLE=-1 \
  BANPROXY_MAXWAIT=30000 \
  BANSSUSER_USERNAME=ban_ss_user \
  BANSSUSER_INITALSIZE=25 \
  BANSSUSER_MAXTOTAL=600 \
  BANSSUSER_MAXIDLE=-1 \
  BANSSUSER_MAXWAIT=30000

ENV CATALINA_OPTS="-server -Xms\$XMS -Xmx\$XMX -Duser.timezone=\$TIMEZONE -Doracle.jdbc.autoCommitSpecCompliant=false"

RUN curl -fSL https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -o /tmp/epel-release-latest-7.noarch.rpm \
  && yum install /tmp/epel-release-latest-7.noarch.rpm -y \
  && yum install xmlstarlet -y \
  && rm -rf /var/cache/yum

RUN cd /usr/local/tomcat/lib/ \
  && curl https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/ojdbc7/12.1.0.2/ojdbc7-12.1.0.2.jar -o ojdbc7.jar \
  && curl https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/ojdbc7/12.1.0.2/ojdbc7-12.1.0.2.jar.sha1 --output ojdbc7.jar.sha1 \
  && echo -n "  ojdbc7.jar" >> ojdbc7.jar.sha1 \
  && sha1sum -c ojdbc7.jar.sha1 \
  && curl https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/xdb6/12.1.0.2/xdb6-12.1.0.2.jar -o xdb6.jar \
  && curl https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/xdb6/12.1.0.2/xdb6-12.1.0.2.jar.sha1 --output xdb6.jar.sha1 \
  && echo -n "  xdb6.jar" >> xdb6.jar.sha1 \
  && sha1sum -c xdb6.jar.sha1 \
  && rm *.sha1 \
  && chown tomcat:tomcat ojdbc7.jar xdb6.jar && chmod +r ojdbc7.jar xdb6.jar

# TLS certs in tomcat
RUN mkdir -p /usr/local/tomcat/tls
COPY --chown=tomcat:tomcat --from=TLS /tls/key.pem /usr/local/tomcat/tls/key.pem
COPY --chown=tomcat:tomcat --from=TLS /tls/server.crt /usr/local/tomcat/tls/server.crt

COPY context.xml /usr/local/tomcat/conf/context.xml
COPY server.xml /usr/local/tomcat/conf/server.xml
COPY run.sh /usr/local/tomcat/bin

# Configure logging to forward tomcat logs to docker log collector
COPY logging.properties /usr/local/tomcat/conf/logging.properties
RUN ln -s /dev/stderr /usr/local/tomcat/logs/localhost.log
RUN ln -s /dev/stderr /usr/local/tomcat/logs/stacktrace.log

RUN mkdir -p /opt/banner/config && mkdir -p /opt/banner/images && chown -R tomcat:tomcat /opt/banner

RUN chown -R tomcat:tomcat $CATALINA_HOME && chmod +x /usr/local/tomcat/bin/run.sh

EXPOSE 8080
EXPOSE 8443
EXPOSE 8009

USER tomcat
CMD ["bin/run.sh"]
