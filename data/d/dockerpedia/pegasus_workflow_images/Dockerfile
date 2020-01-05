FROM ubuntu:16.04

LABEL maintainer "Maximiliano Osorio <mosorio@inf.utfsm.cl>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        gnupg \
        software-properties-common

RUN  DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:openjdk-r/ppa \
     && apt-get update -y \
     && apt-get install -y openjdk-7-jdk \
     &&  wget -O - http://download.pegasus.isi.edu/pegasus/gpg.txt | apt-key add - && \
        echo 'deb http://download.pegasus.isi.edu/wms/download/debian stretch main' > \
        /etc/apt/sources.list.d/pegasus.list  \
     &&  apt-get update -y  \
     && wget https://download.pegasus.isi.edu/pegasus/ubuntu/dists/xenial/main/binary-amd64/pegasus_4.8.5-1+ubuntu16_amd64.deb \
     && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
		./pegasus_4.8.5-1+ubuntu16_amd64.deb \
	 	condor \
     && rm pegasus_4.8.5-1+ubuntu16_amd64.deb \
     && rm -rf /var/lib/apt/lists/*

ENV WORKFLOW_USER workflow
ENV GID 1000
ENV UID 1000
ENV PASS 123456

RUN apt-get update && apt-get install -y --no-install-recommends \
        openssh-server \
        supervisor && \
    groupadd -g ${GID} ${WORKFLOW_USER} && \
    useradd -m -u ${UID} -g ${GID} ${WORKFLOW_USER} && \
    usermod -a -G condor ${WORKFLOW_USER} && \
    echo "root:${PASS}" | chpasswd  && \
    mkdir /home/${WORKFLOW_USER}/example && \
    mkdir -p /run/sshd/ /run/condor && \
    chown condor:condor /run/condor && \
    rm -f /etc/localtime && \
    ln -s /usr/share/zoneinfo/America/Chicago /etc/localtime && \
    rm -rf /var/lib/apt/lists/* && \
    chmod o+rw /opt/

COPY condor_config.docker_image /etc/condor/config.d/
COPY start-condor.sh /usr/sbin/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

USER ${WORKFLOW_USER}
RUN mkdir ~/.ssh/ && \
    chmod 700 ~/.ssh/ && \
    ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa -q -N "" && \
    cat ~/.ssh/id_rsa.pub >>  ~/.ssh/authorized_keys && \
    chmod 600 ~/.ssh/authorized_keys && \
    echo "Host *\nStrictHostKeyChecking no\nUserKnownHostsFile=/dev/null" > ~/.ssh/config

USER root
VOLUME ["/home/${WORKFLOW_USER}/out"]
WORKDIR /home/${WORKFLOW_USER}/
CMD ["/usr/bin/supervisord"]
