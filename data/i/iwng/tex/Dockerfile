FROM paperist/alpine-texlive-ja:latest

RUN tlmgr update --self \
    && tlmgr install braket

WORKDIR /root/docs

CMD [ "/bin/sh" ]
