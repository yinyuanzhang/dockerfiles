FROM selenium/standalone-firefox-debug:2.45.0

 RUN \
   apt-get update && \
   DEBIAN_FRONTEND=noninteractive \
     apt-get install -y --no-install-recommends \
       daemontools \
       inotify-tools \
       moreutils \
   && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/*
  
ADD entry_point.sh /opt/bin/entry_point.sh
ADD cloe_run /usr/local/bin/cloe_run
  
RUN \
  chmod +x /opt/bin/entry_point.sh \
  /usr/local/bin/cloe_run

ENTRYPOINT [ "/opt/bin/entry_point.sh" ]
