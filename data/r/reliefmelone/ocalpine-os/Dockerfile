FROM ebits/openshift-client:latest

LABEL maintainer=relief.melone@gmail.com
LABEL description="Based on ebits/openshift-client but changed the KUBECONFIG so the container is able to run on openshift"

ENV KUBECONFIG "/home/rm-os/.kube/config"

RUN mkdir /home/rm-os && \
    chgrp root -R /home/rm-os && \
    chmod 770 /home/rm-os

USER 1001


