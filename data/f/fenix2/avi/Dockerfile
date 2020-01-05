#auto-builds image on dockerhub
#pull and run in the same directory with the playbooks
#docker pull fenix2/avi:avitools2
#docker run --rm -it -v "$(pwd)":"/ansible" -w="/ansible" fenix2/avi:avitools2 bash

FROM avinetworks/avitools:18.2.6.post1

ENV ANSIBLE_HOST_KEY_CHECKING False
ENV ANSIBLE_FORCE_COLOR True

RUN echo '"\e[A":history-search-backward' >> /root/.inputrc
RUN echo '"\e[B":history-search-forward' >> /root/.inputrc
RUN echo 'alias ll="ls -lA"' >> /root/.bashrc
RUN echo 'export PS1="\[\e[38;5;231m\]\A\[\e[m\]\[\e[38;5;46m\][avi_ansible_container]\[\e[m\]\[\e[38;5;245m\]\w \[\e[m\]\[\e[38;5;250m\]# \[\e[m\]"' >> /root/.bashrc


RUN rm -rf /root/.ansible/roles/avinetworks.avise_csp
RUN git clone https://github.com/avinetworks/ansible-role-avise-csp.git /root/.ansible/roles/avinetworks.avise_csp