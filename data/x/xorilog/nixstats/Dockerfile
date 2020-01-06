FROM debian:jessie
COPY ["install.sh", "entrypoint.sh", "/root/"]
RUN apt-get update && \
    apt-get install -y apt-utils cron wget && \
    cd /root && \
    bash install.sh && \
    apt-get remove -y wget apt-utils make gcc xz-utils build-essential && \
    apt-get autoremove -y && \
    apt-get clean
    
ENTRYPOINT ["/root/entrypoint.sh"]
