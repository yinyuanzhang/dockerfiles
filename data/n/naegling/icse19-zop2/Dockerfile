FROM naegling/icse19-zop2:base
MAINTAINER Richard Rutledge <rrutledge@gatech.edu>

USER zopuser
WORKDIR /home/zopuser

COPY INSTALL.txt /home/zopuser
COPY LICENSE.txt /home/zopuser
COPY README.md /home/zopuser
COPY STATUS.txt /home/zopuser
COPY icse2019-zop2.pdf /home/zopuser
COPY icse2019-zop2-updated.pdf /home/zopuser

USER root
RUN chown zopuser:zopuser /home/zopuser/*

USER zopuser
