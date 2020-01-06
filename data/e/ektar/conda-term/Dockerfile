from ektar/linux-ldap:v1.1.7
MAINTAINER eric@ds-do.com

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
  mini_version="Miniconda3-4.3.31-Linux-x86_64" && \
  wget --quiet https://repo.continuum.io/miniconda/$mini_version.sh -O /tmp/miniconda.sh && \
  mini_md5_expected=$(curl https://repo.continuum.io/miniconda/ 2>/dev/null | \
  grep -A3 Miniconda3-4.3.31-Linux-x86_64 | tail -1 | sed 's/.*>\(.*\)<.*/\1/') && \
  mini_md5=$(md5sum /tmp/miniconda.sh | awk '{print $1}') && \
  /bin/bash -c "[[ '$mini_md5_expected' == '$mini_md5' ]]" && \
  /bin/bash /tmp/miniconda.sh -b -p /opt/conda && \
  rm /tmp/miniconda.sh

# RUN export DEBIAN_FRONTEND=noninteractive && \
#     apt-get update && apt install -qy \
#  && rm -rf /var/lib/apt/lists/*

# COPY startup.sh /data/startup.sh

COPY VERSION /ver-linux-conda-term
