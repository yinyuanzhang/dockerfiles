FROM ligo/base:el7

LABEL name="LIGO Koji Client" \
      maintainer="Adam Mercer <adam.mercer@ligo.org>" \
      date="20190508" \
      support="Best Effort"

# switch to upstream EPEL
RUN yum -y install epel-release && \
      rm /etc/yum.repos.d/lscsoft-epel.repo && \
      rm -rf /var/cache/yum/x86_64/7/lscsoft-epel

# install required packages
RUN yum makecache && \
      yum -y update && \
      yum -y install \
        deltarpm \
        emacs \
        git-lfs \
        git2u \
        koji \
        krb5-workstation \
        ldg-client \
        less \
        mock \
        rpm-build \
        rpmlint \
        sudo \
        vim \
        wget && \
      yum clean all

# setup environment
COPY /environment/sudoers.d/albert /etc/sudoers.d/albert
COPY /environment/koji.conf /etc/koji.conf
COPY /environment/krb5.conf /etc/krb5.conf
COPY /environment/mock /etc/mock
RUN mkdir /container

# setup user
RUN useradd -m -d /container/albert -s /bin/bash albert
RUN su - albert -c "git lfs install"

# enter shell
USER albert
WORKDIR /container/albert
CMD ["/bin/bash", "-l"]
