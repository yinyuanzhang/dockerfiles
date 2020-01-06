#tomcat8.0 dockerfile
FROM tomcat:8.0

# RUN: docker buildするときに実行される
RUN echo "now building..."
# CMD: docker runするときに実行される
CMD echo "now running..."


#vimのインストール
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]


#ポート8080 kaihou
EXPOSE 8080


#java8のインストール

RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886


RUN apt-get update && apt-get clean

RUN apt-get install -y oracle-java8-installer

RUN rm -r /usr/local/tomcat/webapps/ROOT
RUN rm -r /usr/local/tomcat/webapps/docs
RUN rm -r /usr/local/tomcat/webapps/examples
RUN rm -r /usr/local/tomcat/webapps/host-manager
RUN rm -r /usr/local/tomcat/webapps/manager



#アプリケーションデプロイ

ADD gardencityBusGuide.war /usr/local/tomcat/webapps/ROOT.war


#環境変数設定
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV _JAVA_OPTIONS "-Duser.language=ja -Duser.country=JP"
ENV TZ Asia/Tokyo

CMD ["catalina.sh", "run"]
