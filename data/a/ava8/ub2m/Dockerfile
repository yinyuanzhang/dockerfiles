################################################################################
# builder
################################################################################
FROM ava8/ub2b as builder

################################################################################
# merge
################################################################################
FROM ava8/ub2s as system
LABEL maintainer="fcwu.tw@gmail.com"

COPY --from=builder /src/web/dist/ /usr/local/lib/web/frontend/
COPY rootfs /
RUN ln -sf /usr/local/lib/web/frontend/static/websockify /usr/local/lib/web/frontend/static/novnc/utils/websockify && \
	chmod +x /usr/local/lib/web/frontend/static/websockify/run

RUN echo $(date "+%Y-%m-%d_%H:%M:%S" ) > /usr/buildTimeMark \
    && chgrp -R 0 /usr /bin /tmp /home /etc /root /startup.sh /var /run \
    && chmod -R g+rwx /usr /bin /tmp /home /etc /root /startup.sh /var /run
# /src

EXPOSE 80
WORKDIR /root
ENV HOME=/home/ubuntu \
    SHELL=/bin/bash
# HEALTHCHECK --interval=30s --timeout=5s CMD curl --fail http://127.0.0.1:6079/api/health
ENTRYPOINT ["/startup.sh"]
USER 1001