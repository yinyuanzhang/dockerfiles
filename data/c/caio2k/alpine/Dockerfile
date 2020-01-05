FROM alpine
MAINTAINER caio2k

###installing needed packages for sshd, scp, sudo and supervisord
RUN apk update &&\
    apk add openssh supervisor sudo &&\
    rm -rf /var/cache/apk/*

###supervisord config
RUN mkdir -p /var/log/supervisor/ /etc/supervisord.conf.d/
RUN echo -e '[include]\nfiles = /etc/supervisord.conf.d/*.ini\n[supervisord]\npidfile = /var/run/supervisord.pid\nlogfile = /var/log/supervisor/supervisord.log\nloglevel = debug\n[supervisorctl]\nserverurl = unix:///tmp/supervisor.sock\n[rpcinterface:supervisor]\nsupervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface\n[unix_http_server]\nfile = /tmp/supervisor.sock\n' > /etc/supervisord.conf

###ssh config
RUN mkdir /var/run/sshd
#RUN ssh-keygen -A
RUN for i in dsa rsa ecdsa ed25519; do ssh-keygen -q -f /etc/ssh/ssh_host_${i}_key -N '' -t $i; done
RUN sed -i -r 's/.?UseDNS\syes/UseDNS no/' /etc/ssh/sshd_config && sed -i -r 's/.?ChallengeResponseAuthentication.+/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config && sed -i -r 's/.?PermitRootLogin.+/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo -e '[program:sshd]\ncommand=/usr/sbin/sshd -D\nstdout_logfile=/var/log/sshd.log\nstderr_logfile=/var/log/sshd.log\n' > /etc/supervisord.conf.d/sshd.ini


#user config 
ENV USER_NAME     vagrant
ENV USER_PASSWORD vagrant
RUN adduser -S $USER_NAME
RUN echo "$USER_NAME:$USER_PASSWORD" | chpasswd
###sudo config for user
RUN echo -e "Defaults !requiretty \n$USER_NAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/vagrant
USER $USER_NAME
RUN mkdir -p /home/$USER_NAME/.ssh && chmod 700 /home/$USER_NAME/.ssh
###ssh config for user, adding insecure_private_key
RUN echo 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key' > /home/$USER_NAME/.ssh/authorized_keys
RUN chmod 600 /home/$USER_NAME/.ssh/authorized_keys



#docker setup
EXPOSE 22
USER root
#ENTRYPOINT ["/usr/sbin/supervisord", "-c", "/etc/supervisord.conf"]
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]

