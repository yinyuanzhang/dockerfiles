FROM java:8
MAINTAINER l.bennardis@email.it
VOLUME /tmp
RUN mkdir /temp
RUN git clone -b qualityassurance https://github.com/lbennardis/bookabatteryservice.git /temp 
RUN bash -c 'touch /temp/it/luigibennardis/00D-bookABattery_SERVICE/1.3.0.RELEASE/00D-bookABattery_SERVICE-1.3.0.RELEASE.jar'
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/temp/it/luigibennardis/00D-bookABattery_SERVICE/1.3.0.RELEASE/00D-bookABattery_SERVICE-1.3.0.RELEASE.jar"]


 