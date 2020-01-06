FROM rb2nem/nis


RUN sed -i -e 's#%(here)s#/tmp#' /etc/supervisord.conf && \
    sed s#nem:x.*#nem:x:\${USER_ID}:\${GROUP_ID}::\${HOME}:/bin/bash#g /etc/passwd > /.passwd.template && \
    sed s#root:x:0:#root:x:0:0,\${USER_ID}:#g /etc/group > /.group.template && \
    mkdir /projects && \
    for f in /home/nem/ /etc/passwd /etc/group /projects/; do \
      chgrp -R 0 $f && \
      chmod -R g+rwX $f; \
    done

VOLUME /projects
VOLUME /home/nem

COPY [ "entrypoint.sh", "/entrypoint.sh" ]

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "/usr/bin/supervisord" ]
