FROM bioconductor/release_core2

LABEL version="2.2"

ADD install_zUMIs_dep.R /tmp

WORKDIR /soft/

RUN apt-get update -y && \
    apt-get install -y build-essential samtools rna-star pigz curl && \
	Rscript --no-save --no-restore --slave /tmp/install_zUMIs_dep.R

RUN curl --silent -LO https://github.com/sdparekh/zUMIs/archive/zUMIs2.2.tar.gz && \
    tar xvf zUMIs2.2.tar.gz && \
    rm /soft/zUMIs-zUMIs2.2/ExampleData/*.bam && \
    ln -s /soft/zUMIs-zUMIs2.2/zUMIs-master.sh /usr/local/bin
	
CMD zUMIs-master.sh
