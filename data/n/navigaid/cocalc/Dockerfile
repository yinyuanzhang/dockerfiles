FROM cocalc/src

RUN echo "umask 077" >> /etc/bash.bashrc

### Configuration

COPY login.defs /etc/login.defs
COPY login /etc/defaults/login
COPY nginx.conf /etc/nginx/sites-available/default
COPY haproxy.conf /etc/haproxy/haproxy.cfg
COPY run.py /root/run.py
COPY bashrc /root/.bashrc

CMD /root/run.py

EXPOSE 80 443
