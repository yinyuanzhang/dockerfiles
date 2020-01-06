FROM clojure:openjdk-11-lein

ENV LANG=C.UTF-8 \
    PATH=/opt/conda/bin:${PATH}

RUN   apt-get update \
   && apt-get install -y jq iptables libdevmapper1.02.1 libltdl7 \
   && DEB="docker-ce_18.03.1~ce-0~debian_amd64.deb" \
   && wget https://download.docker.com/linux/debian/dists/jessie/pool/stable/amd64/${DEB} \
   && dpkg -i ${DEB} \
   && rm -f ${DEB} \
   && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /root/miniconda.sh \
   && /bin/bash /root/miniconda.sh -b -p /opt/conda \
   && rm -f /root/miniconda.sh \
   && pip install awscli ansible boto3 \
   && wget https://deb.nodesource.com/setup_11.x -O /root/node.sh \
   && /bin/bash /root/node.sh \
   && rm -f /root/node.sh \
   && apt-get install -y nodejs \
   && apt-get autoremove -y \
   && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
   && adduser --home /home/testrunner --shell /bin/bash --gecos "" --disabled-password testrunner \
   && adduser testrunner docker
