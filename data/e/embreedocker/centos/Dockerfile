## ======================================================================== ##
## Copyright 2009-2017 Intel Corporation                                    ##
##                                                                          ##
## Licensed under the Apache License, Version 2.0 (the "License");          ##
## you may not use this file except in compliance with the License.         ##
## You may obtain a copy of the License at                                  ##
##                                                                          ##
##     http://www.apache.org/licenses/LICENSE-2.0                           ##
##                                                                          ##
## Unless required by applicable law or agreed to in writing, software      ##
## distributed under the License is distributed on an "AS IS" BASIS,        ##
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. ##
## See the License for the specific language governing permissions and      ##
## limitations under the License.                                           ##
## ======================================================================== ##

FROM centos:7.4.1708

RUN yum -y install epel-release
RUN yum -y install sudo gcc-c++ clang vim wget tar git nc cmake make tbb-devel ImageMagick freeglut-devel glfw-devel libXmu-devel libXi-devel

RUN useradd -ms /bin/bash visuser
RUN echo "visuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
ENV HOME=/home/visuser
ADD .ssh $HOME/.ssh
RUN chown -R visuser $HOME/.ssh
RUN chgrp -R visuser $HOME/.ssh
RUN chmod -R og-rwx $HOME/.ssh
USER visuser
WORKDIR $HOME

CMD ["/bin/bash"]

