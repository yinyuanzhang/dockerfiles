FROM postgres@sha256:28b4a1b0d3ae9b38a16c97a4e655bdc13496a304d1a241c531ac1efc2faa7230

RUN apt-get update && apt-get install -y postgresql-11-rum python3-pip postgresql-plpython3-11

RUN pip3 install requests pandas lxml 
