#FROM centos:6
FROM okazakiyuji/centos:c6-m30-j1x
MAINTAINER okazakiyuji
WORKDIR /tmp
# Proxy設定が必要な環境でも動くように
COPY proxy-setting.sh /root/
RUN /root/proxy-setting.sh
ENV JENKINS_HOME="/var/lib/jenkins"
# kanonをインストール
COPY kanon /tmp/kanon
RUN hg clone https://bitbucket.org/okamototk/kanonconductor kanonconductor && \
    cp -r /tmp/kanon/* kanonconductor/ && \
    kanonconductor/kanon-setup && \
    cp -fr kanonconductor/resource/jenkins-config/* $JENKINS_HOME && \
    chown jenkins.jenkins -R $JENKINS_HOME && \
    rm -rf /tmp/kanonconductor /tmp/kanon 
# マウント場所のファイルの退避
RUN mkdir -p /tmp/save && cd /tmp/save && \
    cp -r /var/opt/kanon ./var && \
    cp -r /etc/opt/kanon ./etc && \
    cp -r /opt/kanon ./opt && \
    cp -r $JENKINS_HOME ./jenkins
# マウントする場所
VOLUME /opt/kanon
VOLUME /etc/opt/kanon
VOLUME /var/opt/kanon
VOLUME /var/lib/jenkins
# ホストに接続するポート
EXPOSE 80
#  Kanonでリーバースプロキシの設定があるが…
EXPOSE 8080
# Maven動作確認用のファイルをコピーする
COPY maven-test/* /tmp/
WORKDIR /opt/kanon
# Proxy関連の設定を元に戻す
RUN /root/proxy-setting.sh revert
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]
