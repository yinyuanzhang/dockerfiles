FROM ubuntu:trusty
RUN apt-get update && apt-get upgrade -y && apt-get install -y ed ssh ntp rsyslog fail2ban openssh-server openssh-client supervisor python-pyinotify libpam-google-authenticator && apt-get clean
ENV DEBIAN_FRONTEND noninteractive

# Enable google-auth
RUN sed -i '2i auth [success=done new_authtok_reqd=done default=die] pam_google_authenticator.so nullok' /etc/pam.d/sshd
RUN sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes\nAuthenticationMethods publickey,keyboard-interactive/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin no/' /etc/ssh/sshd_config
RUN useradd user 
RUN sudo usermod -s /bin/bash user

# Set up directories
RUN mkdir -p /var/run/sshd /var/log/supervisor /var/run/fail2ban /home/user/.ssh

COPY fail2ban-supervisor.sh /usr/local/bin/
COPY supervisor.d/* /etc/supervisor/conf.d/
COPY fail2ban/* /etc/fail2ban/
ADD copyscript.sh /
RUN chown -R user:user /home/user/
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"] 
EXPOSE 22
