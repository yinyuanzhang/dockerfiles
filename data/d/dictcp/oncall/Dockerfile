FROM ubuntu:16.04

RUN apt-get update && \ 
    apt-get -y install curl python-pip uwsgi unzip virtualenv sudo python-dev libyaml-dev libsasl2-dev libldap2-dev nginx uwsgi-plugin-python mysql-client && \
    rm -rf /var/cache/apt/archives/*

RUN mkdir /tmp/repo
ADD src /tmp/repo/src/
ADD setup.py /tmp/repo/setup.py
ADD db /tmp/repo/db/
ADD ops /tmp/repo/ops/
ADD configs /tmp/repo/configs/

RUN useradd -m -s /bin/bash oncall && \
   chown -R oncall:oncall /home/oncall /var/log/nginx /var/lib/nginx && \
   mkdir -p /home/oncall/var/log/uwsgi /home/oncall/var/log/nginx /home/oncall/var/run && \
   chown oncall /home/oncall/var/log/uwsgi /home/oncall/var/log/nginx /home/oncall/var/run && \
   mv /tmp/repo /home/oncall/source && \
   chown -R oncall:oncall /home/oncall/source && \
   mv /home/oncall/source/ops/config/systemd/uwsgi-oncall.service /etc/systemd/system/uwsgi-oncall.service && \
   mv /home/oncall/source/ops/config/systemd/nginx-oncall.service /etc/systemd/system/nginx-oncall.service && \
   mv /home/oncall/source/ops/config/systemd/nginx-oncall.socket /etc/systemd/system/nginx-oncall.socket

USER oncall

RUN ln -s /home/oncall/source/ops/daemons /home/oncall/daemons && \
    ln -s /home/oncall/source/ops/entrypoint.py /home/oncall/entrypoint.py && \
    ln -s /home/oncall/source/db /home/oncall/db && \
    mkdir /home/oncall/config && \
    cp /home/oncall/source/configs/config.yaml /home/oncall/config/config.yaml && \
    virtualenv /home/oncall/env && \
    /bin/bash -c 'source /home/oncall/env/bin/activate && cd /home/oncall/source && pip install .' && \
    mv -f /home/oncall/daemons/uwsgi-docker.yaml /home/oncall/daemons/uwsgi.yaml && \
    cp /home/oncall/source/configs/config.docker.yaml /home/oncall/config/config.yaml

EXPOSE 8080
CMD ["bash", "-c", "source /home/oncall/env/bin/activate && python /home/oncall/entrypoint.py"]
