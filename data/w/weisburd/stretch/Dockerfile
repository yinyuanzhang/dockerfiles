FROM weisburd/base-image:v1

MAINTAINER Ben Weisburd

# based on https://github.com/Oshlack/STRetch/wiki/Installing-STRetch
ENV VERSION=0.3.4

# clone STRetch
RUN wget "http://github.com/Oshlack/STRetch/archive/v${VERSION}.tar.gz" \
    && tar xzfv v${VERSION}.tar.gz \
    && rm v${VERSION}.tar.gz

WORKDIR /STRetch-${VERSION}

RUN ln -s /STRetch-${VERSION} /STRetch


# prevent install.sh from downloading the 8Gb reference data zip - this should be downloaded outside the docker image
RUN mkdir -p reference-data && touch reference-data/hg19.PCRfreeWGS_143_STRetch_controls.tsv

RUN ./install.sh

RUN rm -rf reference-data/

# install bwa
RUN wget https://github.com/lh3/bwa/archive/master.zip -O bwa.zip \
	&& unzip bwa.zip \
	&& cd bwa-master \
	&& make \
	&& cp bwa /STRetch/tools/bin/ \
	&& cd .. \
	&& rm -rf bwa*

COPY PCRfreeWGS.controls.tsv /
COPY pipeline_config.groovy ./pipelines/
COPY scripts/*.py ./scripts/

COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/bwa /usr/local/bin/bwa
COPY --from=weisburd/base-bam-tools:latest  /picard.jar /picard.jar
COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/samtools /usr/local/bin/samtools
COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/tabix /usr/local/bin/tabix
COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/bgzip /usr/local/bin/bgzip
COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/bcftools /usr/local/bin/bcftools

COPY --from=weisburd/base-vcf-tools:latest  /gatk.jar /gatk.jar
COPY --from=weisburd/base-vcf-tools:latest /usr/local/bin/vt /usr/local/bin/vt

COPY --from=weisburd/base-other-tools:latest  /trf409.linux64  /trf409.linux64
COPY --from=weisburd/base-other-tools:latest /usr/local/bin/bedtools /usr/local/bin/bedtools

COPY --from=weisburd/base-scripts:latest  /scripts /scripts
ENV PYTHONPATH=/scripts:$PYTHONPATH