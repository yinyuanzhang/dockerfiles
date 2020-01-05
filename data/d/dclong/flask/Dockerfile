FROM dclong/python

RUN pip3 install \
        Flask \
        Flask-Bootstrap \
        pandas

COPY scripts /scripts

EXPOSE 80
EXPOSE 5000

ENTRYPOINT ["/scripts/sys/init.sh"]
