FROM openjdk:8u181

RUN apt-get update \
  && apt-get install -y curl tree \
  && apt-get install -y tree \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && useradd -ms /bin/bash liferay 
  

ENV LIFERAY_HOME=/liferay
ENV LIFERAY_SHARED=/storage/liferay
ENV LIFERAY_CONFIG_DIR=/tmp/liferay/configs
ENV LIFERAY_DEPLOY_DIR=/tmp/liferay/deploy
ENV LIFERAY_TOMCAT_URL=https://nchc.dl.sourceforge.net/project/lportal/Liferay%20Portal/7.1.0%20GA1/liferay-ce-portal-tomcat-7.1.0-ga1-20180703012531655.zip
ENV CATALINA_HOME=$LIFERAY_HOME/tomcat-9.0.6
ENV PATH=$CATALINA_HOME/bin:$PATH
ENV GOSU_VERSION 1.11
ENV GOSU_URL=https://github.com/tianon/gosu/releases/download/$GOSU_VERSION



WORKDIR $LIFERAY_HOME

RUN mkdir -p "$LIFERAY_HOME" \
    && set -x \
    && curl "$LIFERAY_TOMCAT_URL" -o /tmp/liferay-ce-portal-tomcat-7.1.0-ga1-20180703012531655.zip \
	  && unzip /tmp/liferay-ce-portal-tomcat-7.1.0-ga1-20180703012531655.zip -d /tmp/liferay \
	  && mv /tmp/liferay/liferay-ce-portal-7.1.0-ga1/* $LIFERAY_HOME/ \
	  && rm /tmp/liferay-ce-portal-tomcat-7.1.0-ga1-20180703012531655.zip \
    && rm -fr /tmp/liferay/liferay-ce-portal-7.1.0-ga1 \ 
    && chown -R liferay:liferay $LIFERAY_HOME


RUN wget -O /usr/local/bin/gosu "$GOSU_URL/gosu-$(dpkg --print-architecture)" \
	  && wget -O /usr/local/bin/gosu.asc "$GOSU_URL/gosu-$(dpkg --print-architecture).asc" \
	  && export GNUPGHOME="$(mktemp -d)"
RUN gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu
RUN rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc
RUN chmod +x /usr/local/bin/gosu
RUN gosu --version
RUN gosu nobody true

COPY ./configs/setenv.sh $CATALINA_HOME/bin/setenv.sh
COPY ./entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8080/tcp 
EXPOSE 9000/tcp
EXPOSE 11311/tcp

VOLUME /storage

RUN addgroup liferay root
USER liferay
ENTRYPOINT ["entrypoint.sh"]
CMD ["catalina.sh", "run"]  