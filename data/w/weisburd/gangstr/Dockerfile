FROM weisburd/base-image:v1

MAINTAINER Ben Weisburd

# install GangSTR from https://github.com/gymreklab/GangSTR
ENV GANGSTR_VERSION=2.4
ENV HTSLIB_CFLAGS="-I./htslib-1.9"
ENV HTSLIB_LIBS=" -L$./htslib-1.9 -lhts"
ENV NLOPT_CFLAGS="-I./nlopt-2.4.2"
ENV NLOPT_LIBS=" -L$./nlopt-2.4.2 -lnlopt"
ENV CPPFLAGS="-std=c++98"

ENV LD_LIBRARY_PATH=/usr/local/lib/

RUN wget https://github.com/gymreklab/GangSTR/releases/download/v${GANGSTR_VERSION}/GangSTR-${GANGSTR_VERSION}.tar.gz \
    && tar xzf GangSTR-${GANGSTR_VERSION}.tar.gz \
    && rm GangSTR-${GANGSTR_VERSION}.tar.gz

WORKDIR /GangSTR-${GANGSTR_VERSION}

# switch mirrors for nlopt - the MIT one was down
RUN sed -i "s/http:\/\/ab-initio.mit.edu\/nlopt\/nlopt-2.4.2.tar.gz/https:\/\/downloads.sourceforge.net\/project\/daetools\/gnu-linux-libs\/nlopt-2.4.2.tar.gz/" install-gangstr.sh

RUN ./install-gangstr.sh

COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/samtools /usr/local/bin/samtools
COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/tabix /usr/local/bin/tabix
COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/bgzip /usr/local/bin/bgzip
COPY --from=weisburd/base-bam-tools:latest  /usr/local/bin/bcftools /usr/local/bin/bcftools

COPY --from=weisburd/base-vcf-tools:latest  /gatk.jar /gatk.jar
COPY --from=weisburd/base-vcf-tools:latest /usr/local/bin/vt /usr/local/bin/vt

COPY --from=weisburd/base-other-tools:latest  /trf409.linux64  /trf409.linux64

COPY --from=weisburd/base-scripts:latest  /scripts /scripts
ENV PYTHONPATH=/scripts:$PYTHONPATH

COPY ./pathogenic_repeats /pathogenic_repeats

# remove ENTRYPOINT because cromwell doesn't work when it's defined
#ENTRYPOINT [ "GangSTR" ]
