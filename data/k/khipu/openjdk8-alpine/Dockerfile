FROM khipu/base-alpine
MAINTAINER developers@khipu.com

RUN apk -U add openjdk8 zip unzip fontconfig ttf-dejavu git openssh libstdc++ \
  && rm -rf /var/cache/apk/*

# jvm fixes
RUN sed -i 's/.*networkaddress.cache.ttl=.*/networkaddress.cache.ttl=5/g' /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security \
  && sed -i 's/.*networkaddress.cache.negative.ttl=.*/networkaddress.cache.negative.ttl=5/g' /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security

RUN curl -sSL https://dl.cacerts.digicert.com/DigiCertSHA2SecureServerCA.crt -o /tmp/digicert_sha2_secure_server_ca.crt && keytool -importcert -alias digicert_sha2_secure_server_ca.pem \
    -keystore /etc/ssl/certs/java/cacerts -trustcacerts \
    -file /tmp/digicert_sha2_secure_server_ca.crt -storepass changeit -noprompt

RUN curl -sSL https://dl.cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt -o /tmp/digicert_sha2_extended_validation_server_ca.crt && keytool -importcert -alias digicert_sha2_extended_validation_server_ca.pem \
    -keystore /etc/ssl/certs/java/cacerts -trustcacerts \
    -file /tmp/digicert_sha2_extended_validation_server_ca.crt -storepass changeit -noprompt



