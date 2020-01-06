FROM kemixkoo/debian-git-svn
MAINTAINER Kemix Koo <kemix_koo@163.com>

ENV DEBIAN_FRONTEND noninteractive

ENV java_version 1.8.0_152
ENV JAVA_HOME /opt/jdk

ENV maven_version 3.3.9
ENV MAVEN_HOME /opt/maven

# download JDK8
ARG jdk_filename="jdk-8u152-linux-x64.tar.gz"
ARG jdk_filemd5="20dddd28ced3179685a5f58d3fcbecd8"
ARG jdk_url="http://download.oracle.com/otn-pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/jdk-8u152-linux-x64.tar.gz"
ARG jdk_tmp="/tmp/${jdk_filename}"

# download java, accepting the license agreement
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O ${jdk_tmp} ${jdk_url}
RUN echo "${jdk_filemd5} ${jdk_tmp}" | md5sum -c

RUN tar -zxf ${jdk_tmp}  -C /opt/ \
        && ln -s /opt/jdk${java_version} ${JAVA_HOME}
        
ENV PATH $JAVA_HOME/bin:$PATH
ENV CLASSPATH .:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar

# configure symbolic links for the java and javac executables
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000 \
        && update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 20000


# download maven
ARG maven_filename="apache-maven-${maven_version}-bin.tar.gz"
ARG maven_filemd5="516923b3955b6035ba6b0a5b031fbd8b"
ARG maven_url="http://archive.apache.org/dist/maven/maven-3/${maven_version}/binaries/${maven_filename}"
ARG maven_tmp="/tmp/${maven_filename}"

RUN wget --no-verbose -O ${maven_tmp}  ${maven_url}
RUN echo "${maven_filemd5} ${maven_tmp}" | md5sum -c

# install maven
RUN tar xzf ${maven_tmp}  -C /opt/ \
        && ln -s /opt/apache-maven-${maven_version} ${MAVEN_HOME} \
        && ln -s ${MAVEN_HOME}/bin/mvn /usr/local/bin

ENV PATH ${MAVEN_HOME}/bin:$PATH

# clean 
RUN  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_*

CMD ["mvn", "--version" ]
