FROM docker.io/scico/easybuildor:7.5.1804

ENV EBDIR /opt/apps

ENV LMOD_VER 7.8.2
ENV EASYBUILD_PREFIX ${EBDIR}
ENV EASYBUILD_MODULES_TOOL Lmod

MAINTAINER Lars Melwyn <melwyn (at) scico.io>

USER root
RUN echo -e " \n\
[easyrepo] \n\
name=EasyBuild repo \n\
baseurl=http://repo.scico.io/bdw/centos/7.5.1804/os/x86_64 \n\
enabled=yes \n\
gpgcheck=1" > /etc/yum.repos.d/easyrepo.repo

RUN rpm --import http://repo.scico.io/key/RPM-GPG-KEY-melwyn && yum list >&/dev/null && \
    echo "module use -a "${EB_DIR}"/modules/all" >> /root/.bashrc && \
    yum -y install foss-2018b Python-2.7.15-foss-2018b && yum clean all && chown -R root.root /opt/apps && \
    echo "module load EasyBuild" >> /root/.bashrc  


CMD /bin/bash
