FROM ubuntu:14.04 
MAINTAINER Mr.Mohammed Syed 
RUN sudo apt-get update
RUN sudo apt-get install -y mysql-server
RUN sudo apt-get install -y python-dev libmysqlclient-dev
RUN sudo apt-get install -y python3.4
RUN sudo apt-get install -y python-pip
RUN sudo pip install MySQL-python
RUN sudo apt-get install -y git
RUN sudo pip install Flask==0.10.1
RUN git clone https://github.com/Kuthubshavali/PythonDock.git
RUN mkdir /usr/local/PythonWebApp/
RUN mv PythonDock /usr/local/PythonWebApp/
WORKDIR /usr/local/PythonWebApp/
EXPOSE 5000
