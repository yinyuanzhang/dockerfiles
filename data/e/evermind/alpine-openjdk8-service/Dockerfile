FROM openjdk:8-jre-alpine

RUN \
  apk --no-cache --update add shadow bash python curl && \
  curl -s https://gist.githubusercontent.com/micw/d7c0e34aee751e81c5aa952b29b8631b/raw/f04a1a36d4c02afc4df4d56d5554bea0ebf08508/update_config.py > /usr/local/bin/update_config.py && \
  chmod 0755 /usr/local/bin/update_config.py && \
  useradd service -d /service && \
  sed -i -r 's/^#?networkaddress.cache.ttl=.*/networkaddress.cache.ttl=1/'  /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security && \
  sed -i -r 's/^#?networkaddress.cache.negative.ttl=.*/networkaddress.cache.negative.ttl=1/'  /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security 
