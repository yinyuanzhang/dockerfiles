FROM alpine

COPY build.sh /tmp/build.sh
RUN chmod 700 /tmp/build.sh
RUN /tmp/build.sh

ENTRYPOINT ["sass"]
CMD ["compile"]