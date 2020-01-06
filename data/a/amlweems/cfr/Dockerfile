FROM openjdk:10
LABEL maintainer "Anthony Weems <amlweems@gmail.com>"

ENV VERSION 0.146
ENV SHASUM 6cc41ece70cb463e0a830fe9d68c22836d9eef5c5f7da1d6e8002c08f5b0f59a

RUN wget -q -O /opt/cfr.jar "https://www.benf.org/other/cfr/cfr-${VERSION}.jar" \
 && echo "${SHASUM}  /opt/cfr.jar" | shasum -a 256 -c -

ENTRYPOINT ["java", "-jar", "/opt/cfr.jar"]
