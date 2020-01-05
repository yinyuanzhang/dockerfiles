FROM anapsix/alpine-java:8

RUN apk add --update \
    curl

RUN cd /tmp/ && curl -o GenomeAnalysisTK-3.8-1-g89b7209.tar.bz2 "https://software.broadinstitute.org/gatk/download/auth?package=GATK-archive&version=3.8-1-0-gf15c1c3ef" \
&& bunzip2 GenomeAnalysisTK-3.8-1-g89b7209.tar.bz2 && tar xvf GenomeAnalysisTK-3.8-1-g89b7209.tar \
&& rm GenomeAnalysisTK-3.8-1-g89b7209.tar \
&& mv GenomeAnalysisTK-3.8-1-0-gf15c1c3ef/GenomeAnalysisTK.jar /usr/bin/GenomeAnalysisTK.jar
