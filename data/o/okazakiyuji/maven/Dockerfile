FROM centos:7
MAINTAINER okazakiyuji
RUN localedef -f UTF-8 -i ja_JP /usr/lib/locale/ja_JP.UTF-8
ENV LANG="ja_JP.UTF-8" LANGUAGE="ja_JP:ja" LC_ALL="ja_JP.UTF-8" TZ="Asia/Tokyo"
RUN yum -y update && \
    yum -y install which unzip mysql git svn mercurial \ 
                   python java-1.8.0-openjdk maven && \
    rm -rf /var/cache/yum/* && \
    yum clean all
COPY proxy-setting.sh /root/
WORKDIR /tmp
#RUN /root/proxy-setting.sh
#COPY SampleProject /tmp/SampleProject
#RUN cd SampleProject && \
#    mvn dependency:go-offline clean package install test && \
#    cd .. && rm -r SampleProject
#RUN /root/proxy-setting.sh revert
COPY docker-entrypoint.sh /
WORKDIR /tmp
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]
