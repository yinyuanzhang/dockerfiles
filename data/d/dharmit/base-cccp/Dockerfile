FROM registry.centos.org/dharmit/base

RUN sudo yum -y update && \
    sudo yum install -y git docker epel-release && \
    sudo yum install -y python-ipython python-pip PyYAML && \
    sudo pip install django==1.11.2 psycopg2==2.7.3 && \
    sudo yum clean all && \
    sudo mkdir /tmp/scan && \
    sudo chown -R user:user /tmp/scan && \
    sudo git clone https://github.com/CentOS/container-pipeline-service/ /opt/cccp-service && \
    sudo chown -R user:user /opt/cccp-service

ENV PYTHONPATH /opt/cccp-service

WORKDIR /opt/cccp-service
VOLUME /tmp/scan

CMD ["python", "container_pipeline/workers/linter.py"]
