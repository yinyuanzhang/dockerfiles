FROM bitnami/consul:latest
USER root
ADD import.json /
ADD customRun.sh /
RUN /bin/bash -c 'chmod +x /customRun.sh'
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/customRun.sh"]