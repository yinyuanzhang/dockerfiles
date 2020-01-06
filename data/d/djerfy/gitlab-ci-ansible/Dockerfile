FROM alpine:3.10
LABEL description="Ansible on Alpine 3.10 and Python 2.7" \
      maintainer="Djerfy <djerfy@gmail.com>"

RUN apk -U add gcc make python python-dev openssl-dev && \
    apk -U add py-pip py-cffi py-bcrypt py-cryptography py-pynacl && \
    pip install ansible==2.9.2

CMD ["ansible", "--version"]

