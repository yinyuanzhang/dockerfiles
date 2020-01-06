FROM centos:7.4.1708

# RUN yum -y update && \
RUN yum -y install centos-release-scl && \
    yum-config-manager --enable centos-sclo-rh-testing && \
    yum -y --setopt=tsflags=nodocs groupinstall "Development Tools" && \
    yum -y install --setopt=tsflags=nodocs \
      rh-python36 \
      rh-python36-python-devel \
      rh-python36-python-pip \
      rh-python36-python-setuptools \
      libcurl-devel \
      openssl-devel && \
    yum clean all

ARG NB_USER=jovyan
ARG NB_UID=1000
ARG HOME=/home/jovyan

ENV LANG C.UTF-8

RUN adduser \
    --comment "Default user" \
    --user-group \
    --uid ${NB_UID} \
    ${NB_USER}

ARG JUPYTERHUB_VERSION=0.8.1

ADD requirements.txt /tmp/requirements.txt

ENV PATH opt/rh/rh-python36/root/usr/bin:/opt/rh/rh-python36/root/bin:$PATH

RUN pip install --no-cache-dir --compile --install-option="--with-nss" pycurl==7.43.0 && \
    pip install --no-cache-dir \
         jupyterhub==${JUPYTERHUB_VERSION} \
         -r /tmp/requirements.txt

ADD jupyterhub_config.py /srv/jupyterhub_config.py

ADD z2jh.py /opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/z2jh.py
ADD cull_idle_servers.py /usr/local/bin/cull_idle_servers.py

WORKDIR /srv/jupyterhub

# So we can actually write a db file here
RUN chown ${NB_USER}:${NB_USER} /srv/jupyterhub

# JupyterHub API port
EXPOSE 8081

USER ${NB_USER}
CMD ["jupyterhub", "--config", "/srv/jupyterhub_config.py"]
