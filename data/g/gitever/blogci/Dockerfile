FROM gitever/blog:ci
MAINTAINER gitever
RUN git clone git@github.com:newdee/BlogBackup.git /Blog && \
    . $NVM_DIR/nvm.sh && \
    cd /Blog && \
    npm install 
ADD .git/ /.git/
RUN cd /Blog && \
    . $NVM_DIR/nvm.sh && \
    git pull && \
    hexo clear && \
    gulp && \
    hexo deploy
