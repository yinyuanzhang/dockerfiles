# This Dockerfile is used to build an image capable of running CE Brightside 2.0 core, CICS, Db2, Endevor, and File Master Plus commands
FROM mikebauerca/docker-brightside-2.0-endevor-fmp

# Installs Brightside CICS & Db2 Plugins
USER jenkins
RUN bright plugins install @brightside/cics@1.1.0-next.201809271925
RUN bright plugins install @brightside/db2@1.0.0-next.201810041114

USER root
