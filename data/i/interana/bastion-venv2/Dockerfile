FROM interana/bastion-base:v1 as VENV2

RUN mkdir /root/.virtualenvs
WORKDIR /root/.virtualenvs
COPY requirements.txt requirements.txt
RUN virtualenv -p /usr/bin/python2.7 venv2x && \
    echo "cryptography==2.2.2" > constraints.txt && \
    venv2x/bin/pip install -r requirements.txt -c constraints.txt && \
    rm constraints.txt && \
    rm -rf /root/.virtualenvs/venv2x/local/lib/python2.7/site-packages/OpenSSL/
