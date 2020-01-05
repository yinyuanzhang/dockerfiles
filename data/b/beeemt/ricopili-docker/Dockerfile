FROM centos

LABEL authors="Benedikt Thoma"\
      description="This is a docker image of ricopili. It should be used in conjunction with docker-compose or a similar architecture."

RUN useradd -d /ricopili -U -m -s /bin/bash ricopili

RUN mkdir /ricopili/{bin,deps,refs,log}

RUN yum install -y epel-release && \
    yum install -y libgomp perl bzip2 R mailx python2-pip python-devel perl-IO-Zlib less vim wget git htop pigz && \
    yum clean packages

##################
#Static Variables#
##################
ENV PATH /ricopili/deps/plink:/ricopili/bin:/ricopili/bin/pdfjam:$PATH
ENV rp_perlpackages /ricopili/deps/perl_modules/
ENV RPHOME /ricopili

######################
#Log Creation (loloc)#
######################
RUN cd /ricopili/log && \
    touch /ricopili/log/preimp_dir_info \
    /ricopili/log/impute_dir_info \
    /ricopili/log/pcaer_info \
    /ricopili/log/idtager_info \
    /ricopili/log/repqc2_info \
    /ricopili/log/areator_info \
    /ricopili/log/merge_caller_info \
    /ricopili/log/postimp_navi_info \
    /ricopili/log/reference_dir_info \
    /ricopili/log/test_info \
    /ricopili/log/clumper_info

########
#Config#
########
RUN curl --progress-bar -Lo /ricopili/ricopili.conf https://raw.githubusercontent.com/beeemT/ricopili-docker/master/ricopili.conf

#############
#R libraries#
#############
RUN Rscript -e 'install.packages("rmeta", repos = "http://cran.us.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("rms", repos = "http://cran.us.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("pROC", repos = "http://cran.us.r-project.org", dependencies = TRUE)'


#####################
#Ricopili-References#
#####################
#RUN cd /ricopili/refs && \
#    wget -nv https://personal.broadinstitute.org/sripke/share_links/ggAhKGdW4XNc0XFn4ZA19Cl3PpcWIs_1000GP_Phase3_sr_0517d_pop_EAS_chr23/ALL_v5a.20130502.chrX_1KG_0517.impute.plink.EAS.bed && \
#    wget -nv https://personal.broadinstitute.org/sripke/share_links/ggAhKGdW4XNc0XFn4ZA19Cl3PpcWIs_1000GP_Phase3_sr_0517d_pop_EAS_chr23/ALL_v5a.20130502.chrX_1KG_0517.impute.plink.EAS.bim && \
#    wget -nv https://personal.broadinstitute.org/sripke/share_links/ggAhKGdW4XNc0XFn4ZA19Cl3PpcWIs_1000GP_Phase3_sr_0517d_pop_EAS_chr23/ALL_v5a.20130502.chrX_1KG_0517.impute.plink.EAS.fam && \
#    wget -nv https://personal.broadinstitute.org/sripke/share_links/ouOIbn17POnccuiiFkZRIgasfPLpqL_1000GP_Phase3_sr_0517d_pop_EUR_chr23/ALL_v5a.20130502.chrX_1KG_0517.impute.plink.EUR.bed && \
#    wget -nv https://personal.broadinstitute.org/sripke/share_links/ouOIbn17POnccuiiFkZRIgasfPLpqL_1000GP_Phase3_sr_0517d_pop_EUR_chr23/ALL_v5a.20130502.chrX_1KG_0517.impute.plink.EUR.bim && \
#    wget -nv https://personal.broadinstitute.org/sripke/share_links/ouOIbn17POnccuiiFkZRIgasfPLpqL_1000GP_Phase3_sr_0517d_pop_EUR_chr23/ALL_v5a.20130502.chrX_1KG_0517.impute.plink.EUR.fam
#
#RUN curl --progress-bar -Lo /tmp/refs.tar.gz https://storage.googleapis.com/cloud-ricopili/reference-genotypes/1KG_ref_ricopili.tar.gz && \
#    tar zxvf /tmp/refs.tar.gz -C /ricopili/refs/ && \
#    rm -f /tmp/refs.tar.gz

#######################
#Ricopili-Dependencies#
#######################
RUN curl --progress-bar -Lo /tmp/deps.tgz  https://personal.broadinstitute.org/sripke/share_links/JeklRDhPD6FKm8Gnda7JsUOsMan2P2_Ricopili_Dependencies.1118b.tar.gz/Ricopili_Dependencies.1118b.tar.gz && \
    tar zxvf /tmp/deps.tgz -C /ricopili/deps/ && \
    chmod 755 -R /ricopili/deps/ && \
    rm -f /tmp/deps.tgz

RUN cd /ricopili/deps/bcftools/resources && \
    curl --progress-bar -Lo human_g1k_v37.fasta.gz http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/human_g1k_v37.fasta.gz && \
    pigz -d ./human_g1k_v37.fasta.gz

RUN mkdir /root/.conda/ &&\
    curl --progress-bar -Lo /tmp/Miniconda2-latest-Linux-x86_64.sh https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh && \
    /bin/bash /tmp/Miniconda2-latest-Linux-x86_64.sh -b -f -p /usr/local/ && \
    rm -f /tmp/Miniconda2-latest-Linux-x86_64.sh && \
    cd /ricopili/deps/ldsc/ && \
    curl --progress-bar -Lo env.yml https://raw.githubusercontent.com/beeemT/ricopili-docker/master/env.yml &&\
    conda env create --file env.yml

###################
#Ricopili-Binaries#
###################

#Newest
RUN cd /tmp && \
    git clone https://github.com/beeemT/ricopili.git && \
    mv ./ricopili/rp_bin/* /ricopili/bin/ && \
    chmod 755 /ricopili/bin/ && \
    rm -rf /tmp/ricopili

#Release v0.0.1
#RUN curl --progress-bar -Lo /tmp/bin.tgz https://github.com/Ripkelab/ricopili/archive/v0.0.1.tar.gz && \
#    tar zxvf /tmp/bin.tgz -C /ricopili/ && \
#    mv /ricopili/ricopili-0.0.1/bin/* /ricopili/bin/ && \
#    rm -rf /ricopili/ricopili-0.0.1 && \
#    chmod 755 /ricopili/bin/