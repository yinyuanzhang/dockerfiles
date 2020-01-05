FROM golang

ADD testinfluxdb.tar.gz /go/src

#×°ÔØÖ´ÐÐÈ¨ÏÞ
RUN /bin/sh -c 'cd /go/src/ && chmod a+x testinfluxdb'

EXPOSE 8080

#Ö±½ÓÖ´ÐÐ¿ÉÖ´ÐÐÎÄ¼þ
CMD /bin/sh -c 'cd /go/src/ && ./testinfluxdb'