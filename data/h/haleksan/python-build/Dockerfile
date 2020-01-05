FROM python:2.7
RUN apt-get update \
  && apt-get install -y openssh-server \
  && ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa \
  && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
  && echo "StrictHostKeyChecking no" >> ~/.ssh/config \
  && pip install ConfigParser dill enum34 gnupg psutil pytest pyyaml requests tox wheel \
  && rm -rfv /var/cache/apt
