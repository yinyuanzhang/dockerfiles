FROM ubuntu:16.04

# install all dependencies in OPT
ENV OPT /opt/bundle
ENV PERL5LIB $OPT/lib/perl5:$PERL5LIB
ENV PATH $OPT/bin:$PATH
ENV PATH /root/perl5/perlbrew/perls/perl-5.18.4/bin:$PATH
ENV LD_LIBRARY_PATH $OPT/lib
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV R_LIBS $OPT/R-lib
ENV R_LIBS_USER $R_LIBS

# install dependencies
COPY ./build/install_dependencies.sh /tmp
RUN bash /tmp/install_dependencies.sh

# install pipelines
COPY ./build/install_pipelines.sh /tmp
RUN bash /tmp/install_pipelines.sh

# install FASTA
ENV PATH $OPT/fasta36-36.3.8/bin:$PATH
RUN cd $OPT \
    && wget https://github.com/wrpearson/fasta36/archive/v36.3.8.tar.gz \
    && tar -zxf v36.3.8.tar.gz && rm v36.3.8.tar.gz \
    && cd fasta36-36.3.8/src && make -f ../make/Makefile.linux_sse2 all

# install R dependencies
COPY ./build/install_dependencies.R /tmp
ENV R_PROFILE_USER $OPT/.Rprofile
RUN Rscript /tmp/install_dependencies.R \
    && echo 'library(methods)' >> $OPT/.Rprofile

# patch bug in BRASS (look for gg10) and Battenberg (line 634)
COPY ./patches/get_rg_cns.R ${OPT}/lib/perl5/auto/share/module/Sanger-CGP-Brass-Implement/Rscripts/get_rg_cns.R
COPY ./patches/Implement.pm ${OPT}/lib/perl5/Sanger/CGP/Battenberg/Implement.pm

# install less
RUN apt-get -yqq update --fix-missing && apt-get -yqq install less
RUN chmod a+rx /root

# create a /ifs volume for MSK users
VOLUME ["/ifs", "/gpfs", "/juno", "/data"]
WORKDIR /data
