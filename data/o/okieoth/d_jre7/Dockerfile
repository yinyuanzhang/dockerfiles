FROM debian:8.6

RUN apt-get update && apt-get install -y --force-yes openjdk-7-jre-headless && rm -rf /var/lib/apt/lists/* && find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true && find /usr/share/doc -empty|xargs rmdir || true && rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* && rm -rf /usr/share/lintian/* /usr/share/linda/* /var/cache/man/*





