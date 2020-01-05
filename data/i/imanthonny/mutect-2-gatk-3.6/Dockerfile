FROM anapsix/alpine-java:8

RUN apk add --update \
    curl \
    && rm -rf /var/cache/apk/*

RUN cd /opt/ && curl -o GenomeAnalysisTK-3.6-0-g89b7209.tar.bz2 "https://software.broadinstitute.org/gatk/download/auth?package=GATK-archive&version=3.6-0-g89b7209" \
&& bunzip2 GenomeAnalysisTK-3.6-0-g89b7209.tar.bz2 && tar xvf GenomeAnalysisTK-3.6-0-g89b7209.tar \
&& rm GenomeAnalysisTK-3.6-0-g89b7209.tar 
