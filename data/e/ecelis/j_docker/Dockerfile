FROM centos:7



ENV user apl

RUN yum -y update ; yum -y install wget libedit sudo ; \
  ln -s /usr/lib64/libedit.so.0.0.42 /usr/lib64/libedit.so.2 ; \
  echo '%wheel        ALL=(ALL)       NOPASSWD: ALL' >> /etc/sudoers.d/wheel ; \
  useradd -G wheel ${user} ; \
  yum -y clean all

USER ${user}

WORKDIR /home/${user}

RUN wget http://www.jsoftware.com/download/j806/install/j806_linux64.tar.gz ; \
  tar -xzf j806_linux64.tar.gz ; \
  mkdir /home/${user}/bin ; \
  ln -s /home/${user}/j64-806/bin/jconsole /home/${user}/bin/j ; \
  rm j806_linux64.tar.gz

# ENTRYPOINT should be defined when using the container as an executable.
#ENTRYPOINT j

# CMD will be overridden when running the container with alternative arguments.
CMD ["bin/j"]
