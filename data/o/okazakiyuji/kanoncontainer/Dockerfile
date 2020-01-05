FROM okazakiyuji/centos4kanoncontainer:t20181115
MAINTAINER okazakiyuji
ENV KANON_HOME="/opt/kanon"
# ファイルをコピーします
COPY resource/ /
# SVN用のproxyを設定します
RUN /root/proxy-setting.sh subversion
COPY download/ /tmp/trac-plugins/
RUN cd /tmp/trac-plugins && ./download-plugins.sh /tmp/install/pluginlist
WORKDIR /opt/kanon
RUN virtualenv --distribute "$KANON_HOME"
RUN source bin/activate && \
    cd /tmp/install && ./install-plugins.sh /tmp/install/pluginlist && \
    pip install simplejson 
WORKDIR /var/opt/kanon
RUN mkdir -p trac hg bzr svn git 
RUN chown -R apache:apache /var/opt/kanon
RUN chown -R apache:apache /etc/opt/kanon
RUN chown -R apache:apache /etc/opt/auth
RUN mkdir -p /tmp/save && cd /tmp/save && \
    cp -r /var/opt/kanon ./var && \
    cp -r /etc/opt/kanon ./etc && \
    cp -r /etc/opt/auth ./auth && \
    cp -r /opt/kanon ./opt
EXPOSE 80
VOLUME /opt/kanon
VOLUME /etc/opt/kanon
VOLUME /etc/opt/auth
VOLUME /var/opt/kanon
WORKDIR /opt/kanon
# syslog関連
RUN sed -i /etc/rsyslog.conf \
     -e '/$ModLoad imjournal/s/^/#/' \
     -e 's/$OmitLocalLogging on/$OmitLocalLogging off/' \
     -e '/$IMJournalStateFile/s/^/#/'
RUN sed -i /etc/rsyslog.d/listen.conf -e '/$SystemLogSocketName/s/^/#/' 
RUN sed -i /etc/httpd/conf/httpd.conf \
     -e 's:logs/error_log:|/usr/bin/logger -p local6\.info -t httpd_error:1' \
     -e 's:logs/access_log:|/usr/bin/logger -p local5\.info -t httpd_access:1'
# Proxy設定を元に戻す
RUN /root/proxy-setting.sh revert
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
