FROM python:3.6-jessie

WORKDIR /

RUN apt-get update --fix-missing
RUN apt-get --no-install-recommends -y install \
    git build-essential zlib1g-dev \
    libxml2-dev libexpat-dev postgresql-client libpq-dev ca-certificates \
    nodejs wget unzip libcurl4-openssl-dev

COPY JBROWSE_VERSION /JBROWSE_VERSION

RUN wget --no-clobber https://github.com/GMOD/jbrowse/releases/download/$(cat /JBROWSE_VERSION)-release/JBrowse-$(cat /JBROWSE_VERSION).zip -O /jbrowse_src.zip
RUN unzip -n -d / /jbrowse_src.zip && \
    mv $(ls -d /JBrowse*) /jbrowse_src

RUN (cd /jbrowse_src/ && \
    ./setup.sh && \
    ./bin/cpanm --force JSON Hash::Merge PerlIO::gzip Devel::Size \
    Heap::Simple Heap::Simple::XS List::MoreUtils Exception::Class Test::Warn \
    Bio::Perl Bio::DB::SeqFeature::Store File::Next Bio::DB::Das::Chado && \
    rm -rf /root/.cpan/)

# install gffread to convert gtf to gff
WORKDIR /

RUN wget http://ccb.jhu.edu/software/stringtie/dl/gffread-0.9.10.Linux_x86_64.tar.gz -O gffread.tar.gz
RUN tar zxf gffread.tar.gz
RUN cp /gffread-0.9.10.Linux_x86_64/gffread /usr/bin

#perl Makefile.PL && make && make install

RUN pip install docopt

# this directory should be bound to a directory on the host
RUN mkdir /jbrowse

# these are specific to scc
# create the directories in case OverlayFS support wasn't built in
RUN for d in /mnt/snakemake /scratch /share /project /projectnb /restricted /usr1 /usr2 /usr3 /usr4 /var/spool/sge /data; do rm -rf $d; mkdir $d; done

# /cwd is for mounting the host current working
RUN mkdir /cwd

COPY runscript.sh /
RUN chmod 777 /runscript.sh

ENV PATH="/jbrowse_src/bin:${PATH}"

ENTRYPOINT ["bash","/runscript.sh"]

COPY pyjbrowse.py /usr/bin/pyjbrowse.py
RUN chmod 777 /usr/bin/pyjbrowse.py
