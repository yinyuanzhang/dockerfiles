FROM interana/bastion-base:v1 as VENV3

RUN mkdir /root/.virtualenvs
WORKDIR /root/.virtualenvs
COPY requirements.txt .
RUN python3 -m venv venv3x && \
    venv3x/bin/pip install -r requirements.txt && \
    venv3x/bin/pip install readline azure-cli awscli


