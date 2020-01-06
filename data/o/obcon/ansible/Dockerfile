FROM ubuntu

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:ansible/ansible
RUN apt-get update
RUN apt-get install -y ansible

RUN mkdir -p /etc/ansible && echo "localhost ansible_connection=local" > /etc/ansible/hosts

CMD ["/bin/bash"]
