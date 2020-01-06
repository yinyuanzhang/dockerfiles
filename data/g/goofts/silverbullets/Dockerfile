FROM alpine:edge

MAINTAINER goofts loking.zhao.moshang@icloud.com

ENV HUMMINGBIRDS_VERSION 1.1.2

WORKDIR /root

RUN apk update && apk add --no-cache git && git clone https://github.com/goofts/silverbullets.git && ls -la                && \
    chmod +x /root/silverbullets/setup.sh && sh /root/silverbullets/setup.sh && mkdir -p /usr/lib/gophernotes /julia_depot && \
    jupyter labextension install dask-labextension && jupyter labextension install transient-display-data                  && \
    jupyter labextension install jupyterlab-drawio && jupyter labextension install @jupyterlab/hdf5                        && \
    jupyter labextension install jupyterlab-dash@0.1.0-alpha.3 && jupyter labextension install @krassowski/jupyterlab-lsp  && \
    jupyter labextension install @krassowski/jupyterlab_go_to_definition && ln -snf /usr/bin/vim /usr/bin/vi               && \
    git clone https://github.com/lckr/jupyterlab-variableInspector && cd jupyterlab-variableInspector && npm install       && \
    npm run build && jupyter labextension install . && cd /root && jupyter labextension install @jupyterlab/hub-extension  && \
    npm install -g configurable-http-proxy && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  && npm cache clean -f   && \
    git clone https://github.com/wireghoul/graudit /graudit_depot && ln -s /graudit_depot/graudit /usr/bin/graudit         && \
    chgrp -R jupyter /usr/share/jupyter && chmod -R 2775 /usr/share/jupyter                                                && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*                                             && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/*   && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

ENV PATH /usr/lib/jvm/default-jvm/bin:$PATH
ENV GOPATH /usr/lib/gophernotes

RUN echo -e "\nexport JAVA_HOME=/usr/lib/jvm/default-jvm" | tee -a /etc/profile && \
    echo -e "export PATH=\$JAVA_HOME/bin:\$PATH"          | tee -a /etc/profile && \
    echo -e "export GOPATH=/usr/lib/gophernotes"          | tee -a /etc/profile

SHELL ["/bin/bash", "-c"]

RUN curl -s https://get.sdkman.io | bash && source /root/.sdkman/bin/sdkman-init.sh                                      && \
    sdk install kotlin 1.3.50 && sdk install scala 2.13.0 && mv /root/.sdkman /sdkman                                    && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

SHELL ["/bin/sh", "-c"]

ENV PATH /sdkman/candidates/scala/2.13.0/bin:/sdkman/candidates/kotlin/1.3.50/bin:$PATH

RUN echo -e "\nexport KOTLIN_HOME=/sdkman/candidates/kotlin/1.3.50" | tee -a /etc/profile && \
    echo -e "export PATH=\$KOTLIN_HOME/bin:\$PATH"                  | tee -a /etc/profile && \
    echo -e "\nexport SCALA_HOME=/sdkman/candidates/scala/2.13.0"   | tee -a /etc/profile && \
    echo -e "export PATH=\$SCALA_HOME/bin:\$PATH"                   | tee -a /etc/profile

RUN beakerx install                                                                                                      && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*
    
RUN git clone https://github.com/goofts/spark.git /spark            && \
    pip3 install toree && jupyter toree install --spark_home=/spark && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf          && \
    rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/*      && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN echo -e "\nexport SPARK_HOME=/spark"          | tee -a /etc/profile && \
    echo -e "export PATH=\$SPARK_HOME/bin:\$PATH" | tee -a /etc/profile

RUN install_c_kernel                                                                                                     && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN python3 -m bash_kernel.install                                                                                       && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN python3 -m sshkernel install                                                                                         && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer                         && \
    wget https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.signed.phar.pubkey                    && \
    wget https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.signed.phar                           && \
    composer require react/zmq && php jupyter-php-installer.signed.phar install                                          && \
    composer require nikic/php-parser && composer require designsecurity/progpilot                                       && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN pip2 install pyzmq ipykernel && python -m ipykernel install                                                          && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN echo "install.packages('languageserver', repos='http://cran.us.r-project.org')" | tee -a install.R                   && \
    echo "install.packages('IRkernel', repos='http://cran.us.r-project.org')" | tee -a install.R                         && \
    echo "IRkernel::installspec(user = FALSE)" | tee -a install.R && Rscript install.R                                   && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN go get -u github.com/gopherdata/gophernotes && cp /usr/lib/gophernotes/bin/gophernotes /usr/bin                      && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN gem install cztop iruby && iruby register                                                                            && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN python3 -m ansible_kernel.install                                                                                    && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN jupyter hiveql install                                                                                               && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN npm install ijavascript -g --unsafe-perm && ijsinstall && npm cache clean -f                                         && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf && rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/* && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

RUN mkdir -p /root/.local/share/jupyter/kernels /root/.vim/UltiSnips                   && \
    mkdir -p /home/goofts/.local/share/jupyter  /home/goofts/.jupyter                  && \
    mkdir -p /root/.vim/bundle && ln -snf /home /usr/include/silverbullets             && \
    git clone https://github.com/goofts/silverbullets.git                              && \
    git clone https://github.com/VundleVim/Vundle.vim.git /root/.vim/bundle/Vundle.vim && \
    mv /root/silverbullets/headers            /usr/include/unix                        && \
    mv /root/silverbullets/lib/*              /usr/lib                                 && \
    mv /root/silverbullets/kernels/*          /root/.local/share/jupyter/kernels       && \
    mv /root/silverbullets/settings           /root/.jupyter                           && \
    mv /root/silverbullets/supervisor         /root/.supervisor                        && \
    mv /root/silverbullets/*bullets.sh        /root                                    && \
    mv /root/silverbullets/vimrc              /root/.vimrc                             && \
    cp -rf /root/.local/share/jupyter/kernels /home/goofts/.local/share/jupyter        && \
    cp -rf /root/.jupyter/lab                 /home/goofts/.jupyter                    && \
    chown -R goofts:jupyter /home/goofts                                               && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf                             && \
    rm -rf /root/silverbullets /root/.[ac]* /tmp/* /var/tmp/* /var/cache/apk/*         && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]*

RUN jupyter labextension install @fissio/hub-topbar-buttons && npm cache clean -f && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf                        && \
    rm -rf ./* ./.[a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/*                    && \
    rm -rf /usr/local/share/jupyter/kernels/[^p]* /usr/share/jupyter/kernels/*

EXPOSE 443

CMD sh /root/silverbullets.sh
