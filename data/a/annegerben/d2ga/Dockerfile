FROM alpine:latest
MAINTAINER AGvA

# install packages
RUN apk add --no-cache bash git python3 py3-requests

#install Domoticz-Google-Assistant
RUN git clone https://github.com/DewGew/Domoticz-Google-Assistant 

#create config dir and entry.sh
RUN mkdir -p config 
RUN ln -s /config/config.py /Domoticz-Google-Assistant/config.py
RUN echo "Creating entry.sh" && echo "#!/bin/bash" > /entry.sh && echo ""	>> /entry.sh && echo "if [ ! -f /config/config.py ]; then" >> /entry.sh && echo "cp /Domoticz-Google-Assistant/default_config.py /config/config.py"	>>  /entry.sh && echo "fi" >> /entry.sh && echo "" >> /entry.sh && echo "python3 /Domoticz-Google-Assistant/" >> /entry.sh 
RUN chmod u+x /entry.sh

# ports and volumes
EXPOSE 3030
VOLUME /config

ENTRYPOINT ["/entry.sh"]