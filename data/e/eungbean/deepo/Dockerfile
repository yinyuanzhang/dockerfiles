FROM ufoym/deepo:all-jupyter
EXPOSE 8888 6006-6015 3000

COPY requirements.txt /tmp

WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

RUN apt-get install -y zsh neovim git git-lfs
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting
RUN echo "source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
RUN echo "source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc
RUN curl -sLf https://spacevim.org/install.sh | bash
RUN curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | bash

RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/latex @jupyterlab/git @krassowski/jupyterlab_go_to_definition jupyterlab-drawio @lckr/jupyterlab_variableinspector @krassowski/jupyterlab-lsp
RUN jupyter lab build

RUN pip install python-language-server[all]

#CleanUp
RUN ldconfig && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*

# Language Server for @krassowski/jupyterlab-lsp
COPY server.yml /tmp
CMD ["node","usr/local/share/jupyter/lab/staging/node_modules/jsonrpc-ws-proxy/dist/server.js","--port 3000","--languageServers","/tmp/server.yml"]

WORKDIR /data
