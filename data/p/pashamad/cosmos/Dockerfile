FROM pashamad/devbase-go

# Python path fix
USER root
RUN ln -s /usr/bin/python3 /usr/bin/python

USER devbase
ADD cosmos.sh /dockerbase/
RUN /dockerbase/cosmos.sh
