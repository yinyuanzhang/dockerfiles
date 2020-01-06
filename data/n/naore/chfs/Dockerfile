FROM alpine

ENV SHARE="/home"

COPY chfs /opt/chfs/chfs

RUN chmod +x /opt/chfs/chfs

EXPOSE 80 

CMD /opt/chfs/chfs --rule="::r|root:admin:r:home:rw" --path=$SHARE
