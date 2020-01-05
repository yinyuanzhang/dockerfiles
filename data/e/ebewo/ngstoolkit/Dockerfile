FROM phusion/baseimage


RUN rm -f /etc/service/sshd/down

ADD clone_branch.sh /etc/my_init.d/clone_branch.sh

RUN chmod 755 /etc/my_init.d/clone_branch.sh

RUN apt-get update && \
	apt-get install -y r-base git wget nano byobu python-pip python python2.7-dev python-numpy python-matplotlib python-pandas python-biopython python-rpy2 python-scipy python-xlsxwriter && \
	rm -rf /var/lib/apt/lists/* && \
	apt-get clean && \
	pip install pysam

RUN wget https://cran.r-project.org/src/contrib/irr_0.84.tar.gz && \
    wget https://cran.r-project.org/src/contrib/lpSolve_5.6.13.tar.gz && \
    R CMD INSTALL lpSolve_5.6.13.tar.gz && \
    R CMD INSTALL irr_0.84.tar.gz && \
    rm irr_0.84.tar.gz lpSolve_5.6.13.tar.gz 

RUN echo "export PYTHONPATH="/NGStoolkit"" >> /root/.bashrc && \
    echo "cd /NGStoolkit/" >> /root/.bashrc && \
    echo "git pull" >> /root/.bashrc && \
    echo "[ -r /root/.byobu/prompt ] && . /root/.byobu/prompt   #byobu-prompt#" >> /root/.bashrc && \
    echo "_byobu_sourced=1 . /usr/bin/byobu-launch 2>/dev/null || true" >> /root/.profile

RUN ssh-keyscan -t rsa gitlab.com >> root/.ssh/known_hosts

EXPOSE 22

VOLUME /NGStoolkit /config

