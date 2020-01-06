# 2018-06-17
FROM ubuntu
MAINTAINER JUNHO.LEE<skyblue1294@126.com>
#RUN yum -y -q upgrade
RUN apt-get -y update
RUN apt-get install -y vim
RUN apt-get install -y python3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 150
RUN apt-get install -y python3-pip --fix-missing
RUN apt-get install -y ipython3
RUN pip3 install ipython
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install scipy
RUN pip3 install statsmodels 
RUN pip3 install sympy


RUN mkdir /home/PYKU_Analysis_py3/
#RUN cd /home && git clone https://github.com/StudyGroupPKU/Project-pre.git
#RUN cd /home && git clone https://github.com/StudyGroupPKU/fruit_team.git
#RUN echo 'The PYKU files are from "https://github.com/StudyGroupPKU". Check if you are Authorized.' > /root/README.txt
RUN echo 'Working Directory is here : /home/PYKU_Analysis_py3/' >> /root/README.txt
#RUN echo 'Try to copy "execute_docker_ROOT.py", which is locates on "/home/Project-pre", to "/home/PYKU_Analysis_py3/" for launching PYKU frame' >> /root/README.txt
RUN echo 'alias vi="vim"' >> /root/.bashrc
RUN echo 'alias pyku="cd /home/PYKU_Analysis_py3"' >> /root/.bashrc
RUN echo 'cd /home/PYKU_Analysis_py3' >> /root/.bashrc
RUN echo 'update-alternatives --install /usr/bin/python python /usr/bin/python3 150' >> /root/.bashrc

ENV REFRESHED_AT 2018-06-17
RUN apt-get -y update

