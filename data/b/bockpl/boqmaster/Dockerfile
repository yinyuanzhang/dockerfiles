FROM bockpl/bocompute:develop
#FROM lokalnerepo

EXPOSE 6444/tcp 8000/tcp

RUN \
# Tymczasowa instalacja git-a i ansible w celu uruchomienia playbook-ow
yum -y install yum-plugin-remove-with-leaves && \
yum -y install ansible && \
yum -y install git && \
# Pobranie repozytorium z playbook-ami
cd /; git clone https://github.com/bockpl/boplaybooks.git; cd /boplaybooks && \
# Skasowanie tymczasowego srodowiska git, UWAGA: Brak tego wpisu w tej kolejnosci pozbawi srodowiska oprogramowania narzedziowego less, man itp.:
yum -y remove git --remove-leaves && \
# Instalacja wymagan dla qmastera SOGE
ansible-playbook Playbooks/install_dep_SOGE_qmaster.yml --connection=local --extra-vars "var_host=127.0.0.1" && \
# Instalacja wymagan dla jupyterhub-a
ansible-playbook Playbooks/install_dep_jupyterhub.yml --connection=local --extra-vars "var_host=127.0.0.1" && \
# Skasowanie tymczasowego srodowiska git i ansible
yum -y remove ansible --remove-leaves && \
rm -rf /ansible

# SGE
ADD soge/sgemaster.blueocean-v15 /etc/init.d/

ADD monit/* /etc/monit.d/

# Katalog w ktorymm jest uruchomiony jupyterhub, tam skladowane beda logi
ENV JUPYTERHUB_WORKDIR=/var/run/jupyterhub
ENV JUPYTERHUB_CONFIGDIR=/opt/software/Blueocean/Configs/jupyterhub

CMD ["/bin/bash","-c","/start.sh"]
