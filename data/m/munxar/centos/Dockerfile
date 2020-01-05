FROM ubuntu
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update --fix-missing && apt-get install -y curl ssh rsync
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php php-mbstring php-dom php-curl php-zip php-gd php-mysql php-sqlite3 composer 
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash \
    && source ~/.nvm/nvm.sh \
    && nvm install 10 \
    && nvm alias default 10 \
    && nvm use default \
    && npm -g i yarn
CMD ["/bin/bash"]
