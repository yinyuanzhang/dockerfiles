
# Extension of the ehive-base-ubuntu-18 image 
# here we install some of the programs to run this with 
# Slurm + singularity 

# Note: Do not install modules from any private locations in this version.

FROM tweep/ehive-base-ubuntu-18

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y \
    && apt-get install -y vim awscli cpanminus build-essential libcurl4-openssl-dev

# libcurl4-openssl-dev required for WWW::Curl::Easy / Bio::GNE::Hive::Utils

RUN curl --insecure -L https://cpanmin.us | perl - App::cpanminus
RUN cpanm File::Slurp IPC::System::Simple Module::Build Test::Differences
RUN cpanm -v AWS::CLIWrapper String::Random Switch

# modules for standard pipelines
RUN cpanm -v File::Temp Test::utf8 Test::TempDir::Tiny Test::File Test::Files

RUN cpanm --local-lib=~/perl5 local::lib && eval $(perl -I ~/perl5/lib/perl5/ -Mlocal::lib)
RUN apt-get install libwww-curl-perl

RUN locale-gen --purge en_US en_US.UTF-8
RUN  echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale


