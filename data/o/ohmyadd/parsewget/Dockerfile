FROM python:2.7-alpine

USER root
COPY dist /root/dist


RUN cp /root/dist/wget.py /usr/bin/wget && \
    chmod a+x /usr/bin/wget && \
    cp /root/dist/matchip.py /usr/bin/tftp && \
    cp /root/dist/matchip.py /usr/bin/ftp && \
    cp /root/dist/matchip.py /usr/bin/ftpget && \
    chmod a+x /usr/bin/tftp && \
    chmod a+x /usr/bin/ftp && \
    chmod a+x /usr/bin/ftpget && \
    
    rm -rf /var/cache/*

ENTRYPOINT ["sh"]
