FROM python:3.6-slim
ENV SUDOFILE /etc/sudoers
RUN apt-get update && \
    apt-get upgrade -y --no-install-recommends && \
    apt-get install -y --force-yes --no-install-recommends \
            build-essential \
            sudo \
            locales \
            curl \
            rsyslog \
            logrotate \
            systemd \
            passwd \
            net-tools \
            procps \
            vim \
            git \
            nginx \
            sed \
            openssl \
            openssh-client \
            postgresql-client
RUN pip3 install --upgrade \
         setuptools \
         ansible==2.8.4 \
         virtualenv==16.7.3 \
         circus==0.15.0 \
         tox==3.13.2 \
         passlib==1.7.1

## setup sshd and generate ssh-keys by init script
ENV LANG ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
COPY ./nginx /etc/logrotate.d/nginx
COPY ./logrotate.conf /etc/logrotate.conf
COPY ./syslog /etc/logrotate.d/syslog
RUN mkdir -p /var/run/sshd &&\
    ssh-keygen -A &&\
    useradd -m -s /bin/bash nginx &&\
    echo -e "nginx:nginx" | (passwd -dq nginx) &&\
    sudo chmod u+w ${SUDOFILE} &&\
    echo '%sudo   ALL=(ALL:ALL) NOPASSWD: ALL' >> ${SUDOFILE} &&\
    sudo chmod u-w ${SUDOFILE} &&\
    mkdir -p ~/.ssh &&\
    chmod 700 ~/.ssh &&\
    locale-gen ja_JP.UTF-8 && \
    localedef -f UTF-8 -i ja_JP ja_JP.utf8 &&\
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime &&\
    sed -i -e '/$ModLoad imjournal/s/^/#/' /etc/rsyslog.conf &&\
    sed -i -e 's/$OmitLocalLogging on/$OmitLocalLogging off/' /etc/rsyslog.conf &&\
    sed -i -e '/$IMJournalStateFile/s/^/#/' /etc/rsyslog.conf &&\
    systemctl enable nginx rsyslog logrotate

ENTRYPOINT ["/usr/sbin/sshd", "-D"]
