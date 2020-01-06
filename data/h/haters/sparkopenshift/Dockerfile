FROM gradiant/spark:2.3.2

# makes rsync available to be used inside the image
RUN apk update && apk add rsync openssh

RUN chgrp root /etc/passwd && chmod ug+rw /etc/passwd

EXPOSE 7001 7002 7003 7004 7005 7011 7012 7013 7014 7015 6066 4040 6066 7077 8080 8081 8881 7000 9000 9001

ADD openshift_entrypoint.sh /openshift_entrypoint.sh

# Adds write permisson to rooter group
RUN chmod -R 777 /opt/spark

RUN chmod 555 /openshift_entrypoint.sh

ENTRYPOINT /openshift_entrypoint.sh
