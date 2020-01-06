FROM ava8/ctbase

ADD /entrypoint.sh /ctbase/entrypoint.sh

RUN echo $(date "+%Y-%m-%d_%H:%M:%S" ) > /ctbase/ctid && \
    chgrp -R 0 /ctbase/ /.ssh && \
    chmod -R g+rwx /ctbase/ /.ssh

ENTRYPOINT  /ctbase/entrypoint.sh 

USER 1001
