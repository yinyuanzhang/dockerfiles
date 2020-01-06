# Base image https://hub.docker.com/u/rocker/
FROM cardcorp/r-java:latest

## install debian packages
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
	libxml2-dev \
	libcairo2-dev \
	libsqlite3-dev \
	libmariadbd-dev \
	libpq-dev \
	libssh2-1-dev \
	unixodbc-dev \
	libcurl4-openssl-dev \
	libssl-dev \
	gnupg2

## copy files
COPY install-packages.R install-packages.R

## install R-packages
RUN Rscript install-packages.R
