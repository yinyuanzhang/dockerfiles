FROM luisperlaz/java8-ansible
MAINTAINER luisperlazaro@gmail.com

COPY ansible/role_playbook.yml /tmp/ansible/role_playbook.yml
COPY ansible/roles /tmp/ansible/roles

WORKDIR /tmp/ansible

RUN ansible-playbook -c local role_playbook.yml -e role=jython

ENTRYPOINT ["/bin/bash", "--login"]

WORKDIR /
