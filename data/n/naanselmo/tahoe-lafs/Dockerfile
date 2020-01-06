FROM tahoelafs/base:latest
LABEL maintainer "admin@nunoanselmo.me"

# Define variables
ENV INTRODUCER_FURL=none STATS_GATHERER_FURL=none WEBUI_PORT=none EXPIRE_ENABLED=false RESERVED_SPACE=1G

# Add entrypoint script
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose the ports
EXPOSE 3457
EXPOSE 8000

# Define the volume
VOLUME /data

CMD [ "tahoe", "start", "/data", "--nodaemon", "--logfile=-" ]
ENTRYPOINT [ "/entrypoint.sh" ]

# Cleanup
RUN rm -rf /tahoe-lafs