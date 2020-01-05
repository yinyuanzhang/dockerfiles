FROM felixkazuyade/base-image
RUN echo "Built at" $(date) > /etc/built_at

ENV REFRESHED_AT $(date) 
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV KEYSTORE=$JAVA_HOME/jre/lib/security/cacerts

RUN apt-get update 
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections 
RUN add-apt-repository -y ppa:webupd8team/java 
RUN apt-get update 
RUN apt-get install -y oracle-java8-installer 
run apt-get install -y xmlstarlet
RUN rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/oracle-jdk8-installer

#trusting letsencrypt
RUN wget -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx1.der
RUN wget -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx2.der
RUN wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.der
RUN wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.der
RUN wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.der 
RUN wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.der 
RUN keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias isrgrootx1 -file /tmp/letsencryptauthorityx1.der 
RUN keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias isrgrootx2 -file /tmp/letsencryptauthorityx2.der 
RUN keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx1 -file /tmp/lets-encrypt-x1-cross-signed.der 
RUN keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx2 -file /tmp/lets-encrypt-x2-cross-signed.der
RUN keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx3 -file /tmp/lets-encrypt-x3-cross-signed.der
RUN keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx4 -file /tmp/lets-encrypt-x4-cross-signed.der


WORKDIR /

CMD [ "/bin/bash"]
