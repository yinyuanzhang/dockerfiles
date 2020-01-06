FROM mgibio/samtools:1.3.1
MAINTAINER Thomas B. Mooney <tmooney@genome.wustl.edu>

LABEL \
  version="0.7.4" \
  description="bam-readcount image for use in Workflows"

RUN apt-get update && \
    apt-get install -y \
        cmake \
        patch \
        git

ENV SAMTOOLS_ROOT=/opt/samtools
RUN mkdir /opt/bam-readcount

WORKDIR /opt/bam-readcount
RUN git clone https://github.com/genome/bam-readcount.git /tmp/bam-readcount-0.7.4 && \
    git -C /tmp/bam-readcount-0.7.4 checkout v0.7.4 && \
    cmake /tmp/bam-readcount-0.7.4 && \
    make && \
    rm -rf /tmp/bam-readcount-0.7.4 && \
    ln -s /opt/bam-readcount/bin/bam-readcount /usr/bin/bam-readcount

ENTRYPOINT ["/usr/bin/bam-readcount"]
