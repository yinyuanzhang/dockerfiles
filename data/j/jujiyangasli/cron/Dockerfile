FROM debian:jessie

# add tini
ENV TINI_VERSION v0.14.0

ADD ./build.sh /build.sh
RUN /bin/bash /build.sh && rm /build.sh

ENTRYPOINT [ "/tini", "--" ]
CMD [ "/bin/bash", "/croninit.sh" ]

