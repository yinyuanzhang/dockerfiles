FROM anapsix/alpine-java:7

ADD https://github.com/broadinstitute/mutect/releases/download/1.1.5/muTect-1.1.5-bin.zip /tmp/

RUN cd /opt/ && unzip /tmp/muTect-1.1.5-bin.zip \
	&& rm /tmp/muTect-1.1.5-bin.zip \
	&& mv /opt/muTect-1.1.5.jar /opt/mutect.jar
