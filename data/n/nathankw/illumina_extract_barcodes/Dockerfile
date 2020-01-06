FROM nathankw/python2:2.7.14
LABEL maintainer "Nathaniel Watson nathankw@stanford.edu"

#Extracts barcodes of interst from the unmatched reads into separate (paired-end) FASTQ files. 
#Folders /srv/src and /srv/software were created in the base image.

#git clone repos
RUN cd /srv/software \
	&& git clone https://github.com/StanfordBioinformatics/illumina_fastq.git
ENV PATH=/srv/software/illumina_fastq/illumina_fastq/scripts:${PATH}
ENV PYTHONPATH=/srv/software/illumina_fastq:${PYTHONPATH}

ENTRYPOINT ["extract_barcodes.py"]
