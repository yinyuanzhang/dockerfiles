FROM ubuntu:14.04

MAINTAINER Ibara Takanashi <ibara1454@gmail.com>

# avoiding error occurs when using apt-get
env DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y texlive texlive-science texlive-lang-cjk latexmk
