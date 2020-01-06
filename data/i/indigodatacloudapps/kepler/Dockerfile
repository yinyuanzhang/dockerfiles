FROM indigodatacloud/ubuntu16.04-sshd:16.04
MAINTAINER Mario David <mariojmdavid@gmail.com>
LABEL description="Container image to run Kepler WF engine"

ARG indigo_kepler_version=v1.2
ARG ansible_role_version=v1.2

RUN ansible-galaxy install indigo-dc.kepler,$ansible_role_version && \
    ansible-playbook --diff /etc/ansible/roles/indigo-dc.kepler/tests/kepler.yml --extra-vars "indigo_kepler_version=$indigo_kepler_version"

EXPOSE 5900
USER indigo
ENV FUTUREGATEWAY_URI 'set_this_when_running_docker'
ENV AUTHORIZATION_TOKEN 'set_this_when_running_docker'
ENV CONFIG_JSON '[{"host":"","port":"","login":"","password":"","argument":""}]'
ENV TOKEN_SERVICE_URI 'set_this_when_running_docker'
ENV TOKEN_SERVICE_USER 'set_this_when_running_docker'
ENV TOKEN_SERVICE_PASSWORD 'set_this_when_running_docker'
CMD /etc/init.d/vmcontext start && \
    /bin/rm --force /tmp/.X0-lock /tmp/.X11-unix/X0 && \
    echo $CONFIG_JSON > /home/indigo/ophidia/ensemble-visualization/phase1/config.json && \
    /usr/bin/vncserver -fg :0
