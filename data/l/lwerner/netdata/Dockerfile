FROM netdata/netdata

ENV NETDATA_PORT=19999 FOO=BAR SMTP_TLS=on SMTP_STARTTLS=on SMTP_SERVER=smtp.gmail.com SMTP_PORT=587 SMTP_FROM=localhost

#ENV NETDATA_STREAM_DESTINATION=tcp:netdata.bunnybase.de:19999
#ENV NETDATA_STREAM_API_KEY=47a060ca-ef43-420f-94df-3561acb8e707
#ENV RESCRAMBLE=1

ADD assets/build.sh /build.sh
RUN chmod +x /build.sh && sync && sleep 1 && /build.sh

ADD assets/run.sh /usr/sbin/run.sh
RUN chmod +x /usr/sbin/run.sh

WORKDIR /

EXPOSE $NETDATA_PORT

#VOLUME /etc/netdata/override

#ENTRYPOINT ["/usr/sbin/run.sh"]
