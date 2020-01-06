FROM meyskens/desktop-base:latest

WORKDIR /tmp

RUN wget https://static.eyskens.me/jdk-8u131-linux-x64.tar.gz
COPY ojdbc7.jar /jars/ojdbc7.jar

#Install the JDK
RUN echo "deb http://httpredir.debian.org/debian/ stretch main contrib" >>/etc/apt/sources.list &&\
    apt-get update && apt-get install -y java-package java-common fakeroot iceweasel &&\
    su -c 'echo y | fakeroot make-jpkg jdk-*' user &&\
    dpkg -i *.deb &&\
    rm -r jdk*

RUN wget http://download.netbeans.org/netbeans/8.2/final/bundles/netbeans-8.2-linux.sh &&\
    chmod +x netbeans-8.2-linux.sh &&\
    ./netbeans-8.2-linux.sh --silent &&\
    rm -rf /tmp/* &&\
    ln -s $(ls -d /usr/local/netbeans-*) /usr/local/netbeans

RUN echo 'netbeans_jdkhome="/usr/lib/jvm/oracle-java8-jdk-amd64"' >>/usr/local/netbeans-8.2/etc/netbeans.conf

ENV TZ="Europe/Brussels"

CMD /usr/local/netbeans/bin/netbeans
