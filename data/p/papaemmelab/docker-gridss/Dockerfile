FROM ubuntu:16.04

ENV PATH /bwa-0.7.17/:$PATH
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# get dependencies
RUN apt-get update \
    && apt-get -y install r-base-core libcurl4-openssl-dev libxml2-dev libssl-dev \
    && apt-get -yqq install openjdk-8-jdk \
    && apt-get -y install wget \
    && wget https://github.com/lh3/bwa/archive/v0.7.17.tar.gz \
    && tar -xvf v0.7.17.tar.gz \
    && cd bwa-0.7.17/ \
    && make \
    && cd .. \
    && mv bwa-0.7.17/bwa bin/
# get gridss
RUN wget https://github.com/PapenfussLab/gridss/releases/download/v2.2.2/gridss-2.2.2-gridss-jar-with-dependencies.jar \
    && R -e 'source("https://bioconductor.org/biocLite.R");biocLite("VariantAnnotation")'

ENV GRIDSS_JAR /gridss-2.2.2-gridss-jar-with-dependencies.jar
VOLUME [ "/gpfs", "/ifs", "/data" ]

COPY run.sh .

CMD ["sh", "/run.sh", "--help"]
ENTRYPOINT ["sh", "/run.sh"]
