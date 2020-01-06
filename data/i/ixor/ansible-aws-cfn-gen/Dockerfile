FROM generik/ansible:v2.6.1

RUN pip install --upgrade pip && \
    pip install "awscli>=1.16,<1.17" && \
    pip install "shyaml"

ADD doit.sh /doit.sh

ENTRYPOINT [ "/doit.sh" ]
