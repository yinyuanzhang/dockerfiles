## Build upon Rocker opensci and add sqlite for Data Carpentry course
FROM rocker/ropensci
MAINTAINER mark.fernandes@cruk.cam.ac.uk

## Refresh package list and upgrade
RUN apt-get update \
  && apt-get install -y sqlite3
