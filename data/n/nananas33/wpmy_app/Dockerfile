FROM mysql:5.7
LABEL version="AC_MY_v2"
WORKDIR /home/anna/ProjetDocker/WPMY_app/MY
COPY toto.txt /tmp
ADD mespaquets.txt .
RUN apt-get update && apt-get install -y iputils-ping
RUN xargs -a mespaquets.txt apt-get install --assume-yes
RUN echo "FIN Installation Paquets MY V2" > /home/anna/ProjetDocker/WPMY_app/MY/Status_Paquets_MY.txt
VOLUME /data/vol_WPMY_DB
ENV my_hostname TICTAC
CMD ["/bin/bash", "-c", "while true; do echo WELCOME on A.C. Mysql Server from $my_hostname and $HOSTNAME V2; sleep 10; done"]
