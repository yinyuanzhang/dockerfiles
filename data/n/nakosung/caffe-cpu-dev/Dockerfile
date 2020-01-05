FROM nakosung/caffe-cpu

RUN apt-get install gdb zsh git-core -y
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh

RUN apt-get install libhiredis-dev -y
RUN apt-get install libzmq3-dev -y

ENTRYPOINT /bin/zsh
