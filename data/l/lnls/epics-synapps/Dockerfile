FROM lnls/epics-base:base-7.0-debian-9.5

ENV COMMIT base-7.0-synapps-lnls-R1-2-1-rev1

RUN git clone https://github.com/lnls-sirius/epics-dev.git /tmp/epics-dev && \
    cd /tmp/epics-dev && \
    git checkout ${COMMIT} && \
    ./run-all.sh -o -i -c -r yes && \
    cd / && \
    rm -rf /tmp/epics-dev && \
    rm -rf /var/lib/apt/lists/*
