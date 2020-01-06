FROM 1science/java:oracle-jre-8

MAINTAINER Ariel Antigua "me@arielantigua.com"

# Download nxcloud
RUN curl -s -L http://www.nxfilter.org/|grep Download \
  |grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*" \
  |grep download|uniq \
  |xargs -n1 curl -s -L \
  |grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*" \
  |grep cloud-.*zip \
  |xargs -n1 wget -q

RUN mkdir /nxcloud \
  && unzip nxcloud* -d /nxcloud \
  && rm -f *.zip \
  && chmod +x /nxcloud/bin/startup.sh

CMD ["/nxcloud/bin/startup.sh"]