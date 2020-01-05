FROM opensciencegrid/osgvo-debian-10:latest

ENV fastgc_version      0.11.8
ENV prokka_version      1.13
ENV quast_version       5.0.2
ENV roary_version       3.12.0
ENV spades_version      3.13.1
ENV trimmomatic_version 0.39

# deps
RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true && \
    apt-get update && \
    apt-get install -y \
        bedtools \
        bioperl \
        cd-hit \
        cpanminus \
        fasttree \
        libdatetime-perl \
        libdigest-md5-perl \
        libxml-simple-perl \
        mafft \
        mcl \
        ncbi-blast+ \
        parallel \
        prank 

# fastqc=0.11.8, https://github.com/s-andrews/FastQC/releases
RUN cd /tmp && \
    curl -o FastQC.zip -L http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${fastgc_version}.zip && \
    unzip FastQC.zip && \
    chmod 755 FastQC/fastqc && \
    mv FastQC /opt

# prokka=1.13, https://github.com/tseemann/prokka/releases
RUN cpanm Bio::Perl && \
    cd /tmp && \
    curl -o prokka-${prokka_version}.tar.gz -L https://github.com/tseemann/prokka/archive/v${prokka_version}.tar.gz && \
    tar xzf prokka-${prokka_version}.tar.gz && \
    rm -f prokka-${prokka_version}.tar.gz && \
    mv prokka-${prokka_version} /opt/prokka
    
# quast=5.0.2, https://sourceforge.net/p/quast/activity/?page=0&limit=100#5bf6d67ee8ba7c12e323f328
RUN export PYTHONPATH=/opt/quast/lib/python2.7/site-packages && \
    mkdir -p /opt/quast/lib/python2.7/site-packages/ && \
    cd /tmp && \
    curl -o quast-${quast_version}.tar.gz -L "https://sourceforge.net/projects/quast/files/quast-${quast_version}.tar.gz/download" && \
    tar xzf quast-${quast_version}.tar.gz && \
    rm -f quast-${quast_version}.tar.gz && \
    cd quast-${quast_version} && \
    python setup.py install --prefix=/opt/quast && \
    cd .. && \
    rm -rf quast-${quast_version}

# roary=3.12.0, https://github.com/sanger-pathogens/Roary/releases
RUN cd /tmp && \
    curl -o Roary-${roary_version}.tar.gz -L https://github.com/sanger-pathogens/Roary/archive/v${roary_version}.tar.gz && \
    tar xzf Roary-${roary_version}.tar.gz && \
    rm -f Roary-${roary_version}.tar.gz && \
    mv Roary-${roary_version} /opt/Roary

# spades=3.13.1, http://cab.spbu.ru/software/spades/
RUN cd /tmp && \
    curl -o SPAdes-${spades_version}-Linux.tar.gz -L http://cab.spbu.ru/files/release${spades_version}/SPAdes-${spades_version}-Linux.tar.gz && \
    tar xzf SPAdes-${spades_version}-Linux.tar.gz && \
    mv SPAdes-${spades_version}-Linux /opt/SPAdes

# trimmomatic=0.39, http://www.usadellab.org/cms/index.php?page=trimmomatic
RUN cd /tmp && \
    curl -o Trimmomatic-${trimmomatic_version}.zip -L http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-${trimmomatic_version}.zip && \
    unzip Trimmomatic-${trimmomatic_version}.zip && \
    rm -f Trimmomatic-${trimmomatic_version}.zip && \
    mv Trimmomatic-${trimmomatic_version} /opt/Trimmomatic 

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

