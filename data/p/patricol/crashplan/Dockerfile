FROM patricol/gui_base:arch


RUN addpackages crashplan-pro \
 && echo "sudo chown user:users /config /cache" >> /scripts/startapp \
 && echo "mkdir -p /config/log /config/conf /config/var /config/metadata" >> /scripts/startapp \
 && echo "sudo /opt/crashplan/bin/CrashPlanEngine start" >> /scripts/startapp \
 && echo "exec CrashPlanDesktop" >> /scripts/startapp \
 && clearcache \
 && sudo mkdir -p /config /cache /usr/local/crashplan \
 && sudo chown user:users /config /cache \
 && mkdir -p /config/var /config/metadata \
 && sudo mv /opt/crashplan/log/ /config/ \
 && sudo mv /opt/crashplan/conf/ /config/ \
 && sudo mv /opt/crashplan/bin/run.conf /config/ \
 && sudo ln -s /config/conf /opt/crashplan/conf \
 && sudo ln -s /config/run.conf /opt/crashplan/bin/run.conf \
 && sudo ln -s /config/log /opt/crashplan/log \
 && sudo ln -s /config/var /var/lib/crashplan \
 && sudo ln -s /config/metadata /usr/local/crashplan/metadata \
 && sudo ln -s /cache /opt/crashplan/cache

VOLUME /config
VOLUME /cache
VOLUME /storage
VOLUME /flash

#if config is missing, copy in defaults
