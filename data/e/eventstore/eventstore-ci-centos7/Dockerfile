FROM centos:7

RUN rpm -Uvh "https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm"

RUN rpm --import "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
RUN curl -s https://download.mono-project.com/repo/centos7-stable.repo | tee /etc/yum.repos.d/mono-centos7-stable.repo

RUN yum update -y && yum install -y mono-devel-5.16.0.220-0.xamarin.4.epel7 msbuild-16.0+xamarinxplat.2018.09.26.17.53-0.xamarin.3.epel7 python pip unzip git rake "dotnet-sdk-2.1"

#NodeJS v8.11.4 (LTS) EOL December 2019
RUN curl -s -o nodejs.rpm https://rpm.nodesource.com/pub_8.x/el/7/x86_64/nodejs-8.11.4-1nodesource.x86_64.rpm && rpm -Uvh nodejs.rpm

#fpm
RUN yum install -y ruby-devel gcc make rpm-build rubygems && gem install --no-ri --no-rdoc fpm

#aws cli
RUN curl -s -o awscli-bundle.zip "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" \
    && unzip awscli-bundle.zip \
    && ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \
    && rm -rf /awscli-bundle \
    && rm awscli-bundle.zip