FROM organizrtools/organizr-v2:latest
ENV LAKKRIS_SERVICE="organizr" \
    LAKKRIS_PORT="80" \
    LAKKRIS_CONFIGFILE="/config/nginx/site-confs/default" \
    LAKKRIS_SERVERNAME="lostlakkris"

EXPOSE 7946

COPY bin/serf_0.8.1_amd64 /usr/sbin/serf
COPY bin/jq_1.6_amd64 /usr/sbin/jq
COPY bin/templater /usr/sbin/templater
#COPY bin/nc_1.27.1_686 /usr/bin/nc

COPY lakkris/ /
