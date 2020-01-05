FROM centos:7.6.1810

RUN yum -y --setopt="tsflags=nodocs" update && \
    yum -y --setopt="tsflags=nodocs" install git maven rpm-build rpm-sign sudo expect wget epel-release && \
    yum -y --setopt="tsflags=nodocs" install jq \
    yum clean all && \
    rm -rf /var/cache/yum/

RUN useradd builder -u 1000 -m -G users,wheel && \
    echo "builder ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    echo "# macros"                      >  /home/builder/.rpmmacros && \
    echo "%_topdir    /home/builder/rpm" >> /home/builder/.rpmmacros && \
    echo "%_sourcedir %{_topdir}"        >> /home/builder/.rpmmacros && \
    echo "%_builddir  %{_topdir}"        >> /home/builder/.rpmmacros && \
    echo "%_specdir   %{_topdir}"        >> /home/builder/.rpmmacros && \
    echo "%_rpmdir    %{_topdir}"        >> /home/builder/.rpmmacros && \
    echo "%_srcrpmdir %{_topdir}"        >> /home/builder/.rpmmacros && \
    mkdir /home/builder/rpm && \
    chown -R builder /home/builder

USER builder
WORKDIR "/home/builder"
ENV FLAVOR=rpmbuild OS=centos DIST=el7
CMD /bin/bash