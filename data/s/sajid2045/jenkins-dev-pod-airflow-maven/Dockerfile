FROM jenkinsxio/builder-maven:latest

RUN lsb_release -a 


RUN localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias fr_FR.UTF-8
ENV LANG fr_FR.utf8

# gcc because we need regex and pyldap
# openldap-devel because we need pyldap
RUN yum update -y \
    && yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum install -y python36u python36u-libs python36u-devel python36u-pip \
    && yum install -y which gcc \ 
    && yum install -y openldap-devel  

# pipenv installation
RUN pip3.6 install pipenv
RUN rm -rf /bin/pip 
RUN ln -s /usr/bin/pip3.6 /bin/pip
RUN rm /usr/bin/python
# python must be pointing to python3.6
RUN ln -s /usr/bin/python3.6 /usr/bin/python

RUN pip install --upgrade pip

WORKDIR /opt/intranet
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes
ADD requirements.txt /root/requirements.txt 
RUN /bin/pip install -r /root/requirements.txt 

COPY m2 /root/.m2

RUN aws --version


