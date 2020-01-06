# Android development environment for ubuntu precise (14.04 LTS).
# version 0.0.1
# Start with ubuntu precise (LTS).
FROM gmetal/android_ndk64
MAINTAINER gmetaxas <gmetaxas@gmail.com>

#Create AOSP source directory
RUN mkdir /usr/local/aosp

#Install required packages
RUN sudo apt-get update && sudo apt-get install -y bison g++-multilib git gperf libxml2-utils curl

#Install the repo
#Make sure you have a bin/ directory in your home directory and that it is included in your path: 
RUN mkdir ~/bin

#Download the Repo tool and ensure that it is executable:
RUN curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
RUN chmod a+x ~/bin/repo

#OpenJDK 1.7 is a requirement for android 5.0
RUN sudo apt-get update && sudo apt-get install -y openjdk-7-jdk
RUN sudo apt-get update && sudo apt-get install -y unzip zip

ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64
RUN export PATH=~/bin:$JAVA_HOME/bin:$PATH

