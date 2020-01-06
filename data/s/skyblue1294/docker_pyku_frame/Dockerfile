# 2018-06-18
FROM skyblue1294/pyku_root
MAINTAINER JUNHO.LEE<skyblue1294@126.com>
ENV REFRESHED_AT 2018-06-18
#RUN yum -y -q upgrade
RUN yum install -y vim
RUN yum install -y evince
RUN yum install -y tkinter
RUN mkdir /home/PYKU_Analysis/
RUN cd /home && git clone https://github.com/StudyGroupPKU/Project-pre.git
RUN cd /home && git clone https://github.com/StudyGroupPKU/fruit_team.git
RUN echo 'The PYKU files are from "https://github.com/StudyGroupPKU". Check if you are Authorized.' > /root/README.txt
RUN echo 'Working Directory is here : /home/PYKU_Analysis/' >> /root/README.txt
RUN echo 'Try to copy "execute_docker_ROOT.py", which is locates on "/home/Project-pre", to "/home/PYKU_Analysis/" for launching PYKU frame' >> /root/README.txt
RUN echo '..TEST..' >> /root/README.txt
RUN echo 'alias vi="vim"' >> /root/.bashrc
RUN echo 'alias pyku="cd /home/PYKU_Analysis"' >> /root/.bashrc
RUN echo 'cd /home/PYKU_Analysis' >> /root/.bashrc
#RUN echo 'alias vi="vim"' >> /home/.bashrc
#RUN echo 'cd /home/PYKU_Analysis' >> /home/.bashrc
