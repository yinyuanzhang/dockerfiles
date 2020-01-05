FROM pihizi/selenium-base:2.44.0
MAINTAINER PiHiZi <pihizi@msn.com>

#========================
# Selenium Configuration
#========================
COPY config.json /opt/selenium/config.json

EXPOSE 4444

USER pihizi

CMD ["java", "-jar", "/opt/selenium/selenium-server-standalone.jar", "-role", "hub", "-hubConfig", "/opt/selenium/config.json"]

