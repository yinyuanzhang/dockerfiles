FROM centos:7
MAINTAINER "Thomas Enzinger <info@thomas-enzinger.de>"

# install software
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm   \
&& yum update -y                                                                            \
&& yum group install "Development Tools" -y                                                 \
&& yum install -y                                                                           \
  make cmake cmake3 autoconf automake binutils bison flex gettext libtool patch             \
  gcc gcc-gfortran gcc-c++ java-1.8.0-openjdk-devel                                         \
  git bc wget curl sudo                                                                     \
  boost-*                                                                                   \
  blas* lapack* hdf5* gsl gsl-devel                                                         \
  perl python python-devel python3 python3-devel                                            \
  openmpi*                                                                                  \
  lesstif lesstif-devel libX11 libXext libXp libXau libXaw libXmu libXt libXpm

# config os
RUN groupadd tefe && useradd -m --shell /bin/bash -g tefe tefe                              \
 && echo "tefe ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers                                      \
 && echo 127.0.1.1 $(hostname) >> /etc/hosts                                                \
 && echo "export OMPI_MCA_btl_vader_single_copy_mechanism=none" >> /root/.bashrc            \
 && echo "export OMPI_MCA_btl_vader_single_copy_mechanism=none" >> /home/tefe/.bashrc

SHELL ["/bin/bash", "-xec"]

ARG SOURCE_COMMIT
ARG VERSION
ARG FILE_SRC
ARG FILE_EXTRACT_NAME
ARG TARGET_NAME
ENV INSTALL_DIR=/opt/$TARGET_NAME

# install
COPY data/$FILE_SRC.md5 /tmp
RUN cd /tmp && \
 wget -q https://dakota.sandia.gov/sites/default/files/distributions/public/$FILE_SRC        \
 -O $FILE_SRC -t 10 -T 30                                                                    \
 && md5sum -c --status ${FILE_SRC}.md5 && tar xzvf $FILE_SRC                                 \
 && mv $FILE_EXTRACT_NAME /opt/$TARGET_NAME                                                  \
 && rm -f ${FILE_SRC} ${FILE_SRC}*

# setup env
RUN echo "export PATH=$INSTALL_DIR/bin:$INSTALL_DIR/share/dakota/test:$INSTALL_DIR/gui:$PATH" >> /home/tefe/.bashrc \
 && echo "export PYTHONPATH=$PYTHONPATH:$INSTALL_DIR/share/dakota/Python" >> /home/tefe/.bashrc

# setup run
VOLUME ["/data"]
WORKDIR /data
USER tefe

#
ENTRYPOINT ["/bin/bash", "-ci"]

