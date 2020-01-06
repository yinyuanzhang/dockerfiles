FROM jboss/keycloak:6.0.1

ENV JBOSS_HOME /opt/jboss/keycloak
ENV THEMES_HOME $JBOSS_HOME/themes
ENV THEMES_VERSION 0.1.3
ENV THEMES_TMP /tmp/keycloak-theme
ENV BINTRAY_URL https://dl.bintray.com/a-k-pohresniy/onotoliy

RUN mkdir -p $THEMES_TMP

ADD $BINTRAY_URL/com/github/onotoliy/opposite/keycloak-theme/$THEMES_VERSION/keycloak-theme-$THEMES_VERSION.jar $THEMES_TMP

USER root

RUN unzip $THEMES_TMP/keycloak-theme-$THEMES_VERSION.jar -d $THEMES_TMP
RUN mv $THEMES_TMP/theme/* $THEMES_HOME

RUN ls -l $THEMES_HOME

RUN chmod -R a+r $JBOSS_HOME

RUN rm -rf $THEMES_TMP

USER jboss
