FROM alpine
RUN apk update
RUN apk add openntpd
RUN mkdir -p /var/empty
COPY ntpd.conf /etc/ntpd.conf
ENTRYPOINT ["ntpd"]
CMD ["-d"]
