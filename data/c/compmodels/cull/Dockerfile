FROM python:3

RUN pip install tornado python-dateutil

RUN mkdir /srv/cull
WORKDIR /srv/cull
ADD https://raw.githubusercontent.com/jupyter/jupyterhub/master/examples/cull-idle/cull_idle_servers.py /srv/cull/cull_idle_servers.py

ENTRYPOINT ["python", "cull_idle_servers.py"]
