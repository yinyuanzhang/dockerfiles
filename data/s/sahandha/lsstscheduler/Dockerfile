FROM python:3.5-slim

MAINTAINER Sahand Hariri sahandha@gmail.com
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
RUN apt-get -qq update
RUN apt-get -qq -y install wget curl
RUN sudo apt-get -qq -y install software-properties-common apt-utils

RUN sudo apt-get install -y python-pip python-dev build-essential
RUN sudo apt-get install -y git
RUN pip install --upgrade pip
RUN pip install git+https://github.com/kubernetes-client/python.git
RUN python -m pip install pymongo

Add kube_deploy.py /kube_deploy.py
Add sched.py /sched.py

RUN apt-get install -y vim; exit 0
