# Dockerfile to for:

# Load miniconda Docker image to work off of
FROM ssidk/bifrost-base:2.0

LABEL \
    name="bifrost-whats_my_species_check" \
    description="Docker environment for whats_my_species in bifrost" \
    version="2.0" \
    DBversion="31/07/19" \
    maintainer="kimn@ssi.dk;"

RUN \
    conda install -yq -c bioconda kraken==1.1.1; \
    conda install -yq -c bioconda bracken==1.0.0; \
    # Kraken mini DB and bracken
    cd /bifrost_resources; \
    # NOTE: even though the file is dated 20171019 it's actually when unzipped 20171013, to avoid some issues im renaming it minikraken
    # wget -q https://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_4GB.tgz; \
    wget -q https://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_8GB.tgz; \
    # tar -zxf minikraken_20171019_4GB.tgz; \
    # The tar contains a folder so just need to change it to minikraken (the -C)
    tar -zxvf minikraken_20171019_8GB.tgz; \
    mv minikraken_20171019_8GB minikraken; \
    rm minikraken_20171019_8GB.tgz; \
    # wget -q https://ccb.jhu.edu/software/bracken/dl/minikraken_4GB_100mers_distrib.txt;
    wget -q https://ccb.jhu.edu/software/bracken/dl/minikraken_8GB_100mers_distrib.txt;\
    mv minikraken_8GB_100mers_distrib.txt minikraken_100mers_distrib.txt;

ENTRYPOINT \
    ["/bifrost_resources/docker_umask_002.sh"]
