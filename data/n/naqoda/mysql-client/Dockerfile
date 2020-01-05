# =============================================================================
# naqoda/centos-apache-php
#
# CentOS-7, MySQL client
# 
# =============================================================================
FROM centos:centos7

MAINTAINER Naqoda <info@naqoda.com>

# -----------------------------------------------------------------------------
# MySQL client
# -----------------------------------------------------------------------------
RUN	yum -y update \
	&& yum --setopt=tsflags=nodocs -y install \
	mysql \
	&& rm -rf /var/cache/yum/* \
	&& yum clean all
