FROM bitnami/minideb:latest

ENV jdkURL https://download.java.net/java/early_access/jdk12/7/GPL/openjdk-12-ea+7_linux-x64_bin.tar.gz

#ENV gradleURL https://services.gradle.org/distributions
#ENV gradleFile gradle-4.8-rc-1-bin.zip

RUN apt-get update && apt-get install -y git wget 
#unzip

RUN mkdir /j # Java central directory

WORKDIR /j

# Install JDK and remove unnecessary data and strip binaries to save space
RUN wget -q -O - ${jdkURL} | tar xzf - --exclude="lib/src.zip" --exclude="legal" --exclude="lib/desktop" --exclude="demo" ; mv jdk-1* jdk && ln -s /j/jdk /j/jdk ; cd /j/jdk 
#; strip lib/*.so lib/server/*.so

# Install Maven
#RUN cd /j ; wget http://apache.mirrors.lucidnetworks.net/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz ; tar xvzf apache-maven-3.5.0-bin.tar.gz ; mv apache-maven-3.5.0 mvn ; rm -f apache-maven-3.5.0-bin.tar.gz


#RUN cd /j ; wget ${gradleURL}/${gradleFile} ; unzip ${gradleFile} ; rm ${gradleFile} ; mv gradle-* gradle ; rm -Rf gradle/media gradle/lib/native-platform-{freebsd,osx,windows}* gradle/lib/*kotlin*

# remove binutils, no longer needed for 'strip'
RUN apt-get purge -y binutils wget  ; apt-get autoclean ; apt-get autoremove ; apt-get clean

# establish paths
ENV PATH=/j/jdk/bin:$PATH
#:/j/gradle/bin:$PATH
