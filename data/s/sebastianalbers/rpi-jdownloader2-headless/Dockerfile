FROM jaymoulin/jdownloader:0.7.0-arm32v6

EXPOSE 9666

COPY start.sh /usr/bin/start-jd-daemon

VOLUME /opt/JDownloader/extensions

CMD ["tini", "--", "start-jd-daemon"]
