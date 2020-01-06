FROM python

RUN pip install requests git+https://github.com/arthaud/python3-pwntools.git

RUN groupadd -r pwn && useradd -r -g pwn pwn
USER pwn

ENV TERM linux