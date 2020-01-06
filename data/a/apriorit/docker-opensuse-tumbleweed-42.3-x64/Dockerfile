# This docker file contains build environment
FROM opensuse/tumbleweed
MAINTAINER Sergii Kusii <kusii.sergii@apriorit.com>

RUN zypper -n in kernel-vanilla-4.19.7-1.5 kernel-vanilla-devel && \
    zypper -n in cmake make gcc-c++ libelf-devel
