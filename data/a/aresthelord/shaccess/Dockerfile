FROM debian:jessie

LABEL maintainer="me@p1ngp0ng.net"
LABEL "forked-from"="https://github.com/opsxcq/exploit-CVE-2014-6271"

RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    apache2 openssh-server supervisor && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor
RUN cp /etc/ssh/sshd_config /etc/ssh/sshd_config.original
RUN chmod a-w /etc/ssh/sshd_config.original


# install packages
COPY packages /packages

RUN dpkg -i /packages/*

# # copy vulnerable script 
# COPY vulnerable /usr/lib/cgi-bin/
#RUN rm -rf /var/www
COPY www /var/www

COPY vulnerable /usr/lib/cgi-bin/
RUN mv /usr/lib/cgi-bin/vulnerable /usr/lib/cgi-bin/status

RUN chown -R www-data:www-data /var/www/
RUN  addgroup -gid 666 ones && \
    (sleep 1;echo "#jH}#bM$m%}gJy2A"; sleep 1;echo "#jH}#bM$m%}gJy2A") |adduser --gid 666 --uid 666 theone 

RUN mkdir /home/theone/.ssh
COPY id_rsa /home/theone/.ssh/
COPY id_rsa.pub /home/theone/.ssh/
COPY authorized_keys /home/theone/.ssh/
RUN chown -R theone /home/theone/.ssh/
RUN chmod 600 /home/theone/.ssh/id_rsa
RUN chmod 644 /home/theone/.ssh/id_rsa.pub
RUN chmod 644 /home/theone/.ssh/authorized_keys

#copy user level flag to directory
COPY p1ng.txt /home/theone/
RUN chown theone /home/theone/p1ng.txt
RUN chmod 660 /home/theone/p1ng.txt

# copy root level flag to directory
COPY p0ng.txt /root/
RUN chown root:root /root/p0ng.txt
RUN chmod 660 /root/p0ng.txt

# arrange for user level escalation
RUN chown theone /var/www/tac
RUN mv /var/www/tac /var/
RUN chmod u+s /var/tac

# create file readable after ssh
RUN mkdir /home/theone/.pp
COPY p0ng.txt /home/theone/.pp/
RUN chown root:ones /home/theone/.pp/p0ng.txt
RUN chmod 640 /home/theone/.pp/p0ng.txt

# disable running commands like shutdown, reboot, halt, poweroff
RUN chmod  o-x /bin/systemctl

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/cgi.load
RUN ln -s /etc/apache2/mods-available/cgid.conf /etc/apache2/mods-enabled/cgid.conf
RUN ln -s /etc/apache2/mods-available/cgid.load /etc/apache2/mods-enabled/cgid.load
RUN ln -sf /dev/null /home/theone/.bash_history
RUN ln -sf /dev/null /var/www/.bash_history
RUN ln -sf /dev/null /root/.bash_history
RUN echo 'set +o history' >> /home/theone/.bash_profile
RUN echo 'unset HISTFILE' >> /home/theone/.bash_profile

# set restricted bash for user theone
# change bash to restricted bash
RUN chsh -s /bin/rbash theone
# create directory for holding executables
RUN mkdir /home/theone/bin
RUN chmod 755 /home/theone/bin
# set PATH to newly created directory
RUN echo "export PATH='/home/theone/bin'" >> /home/theone/.bashrc
RUN echo "export PATH='/home/theone/bin'" >> /home/theone/.bash_profile
# decide which executables are not restricted
RUN ln -s /usr/bin/find /home/theone/bin/
RUN ln -s /bin/su /home/theone/bin/
RUN ln -s /bin/cat /home/theone/bin/
RUN ln -s /bin/ls /home/theone/bin/
RUN ln -s /bin/which /home/theone/bin/
# prevent user to change the file
RUN chmod 640 /home/theone/.bashrc

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 22 80
CMD ["/usr/bin/supervisord"]

