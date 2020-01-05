
FROM node
RUN npm install -g express-generator pm2 gulp-cli browserify karma-cli webpack
RUN apt-get update
RUN apt-get install -y vim tmux net-tools socat less
ADD .vim /root/.vim
ADD .vimrc /root/.vimrc

CMD "/bin/bash"
