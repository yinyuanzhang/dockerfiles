FROM bioportainer/scienv:cuda

ENV PYENV_ROOT $SCIENV_ROOT/envs/pyenv
ENV PYENV $PYENV_ROOT/bin:$PYENV_ROOT/shims:$PYENV_ROOT/envs:$PYENV_ROOT/plugins
ENV PYTHON-BUILD $PYENV_ROOT/plugins/python-build/bin
ENV PYENV-DOCTOR $PYENV_ROOT/plugins/pyenv-doctor/bin
ENV PYENV-INSTALLER $PYENV_ROOT/plugins/pyenv-installer/bin
ENV PYENV-UPDATE $PYENV_ROOT/plugins/pyenv-update/bin
ENV PYENV-VIRTUALENV $PYENV_ROOT/plugins/pyenv-virtualenv/bin
ENV PYENV-WHICH-EXT $PYENV_ROOT/plugins/pyenv-which-ext/bin
ENV PATH $SCIENV_ROOT/bin:$SCIENV_ROOT/envs:$PYENV:$PATH
ENV PYTHON3_VERSION miniconda3-latest
ENV PYTHON2_VERSION miniconda2-latest

USER $USER

RUN scienv install pyenv \
    && echo 'eval "$(pyenv init -)"' >> $HOME/.bash_profile \
    && echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bash_profile \
    && echo 'export PYENV_VIRTUALENV_DISABLE_PROMPT=1' >> $HOME/.bash_profile \
    && echo 'export PYENV_ROOT="$HOME/.scienv/envs/pyenv"' >> $HOME/.bash_profile \
    && echo 'eval "$(pyenv init -)"' >> $HOME/.bashrc \
    && echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bashrc \
    && echo 'export PYENV_VIRTUALENV_DISABLE_PROMPT=1' >> $HOME/.bashrc \
    && echo 'export PYENV_ROOT="$HOME/.scienv/envs/pyenv"' >> $HOME/.bashrc \
    && eval "$($PYENV_ROOT/bin/pyenv init -)" \
    && eval "$($PYENV_ROOT/bin/pyenv virtualenv-init -)" \
    && /bin/bash -c "exec $SHELL -l" \
    && /bin/bash -c "source $HOME/.bashrc" \
    && /bin/bash -c "source $HOME/.bash_profile" \
    && /bin/bash -c "source $PYENV_ROOT/completions/pyenv.bash" \
    && chown -R $USER:$USER $HOME \
    && eval "$(pyenv init -)" \
    && eval "$(pyenv virtualenv-init -)" \
    && pyenv install $PYTHON3_VERSION \
    && pyenv global $PYTHON3_VERSION \
    && pyenv rehash \
    && pyenv activate $PYTHON3_VERSION \
    && conda config --add channels defaults \
    && conda config --add channels conda-forge \
    && conda config --add channels bioconda \
    && conda config --add channels biobuilds \
    && conda update --all && conda clean -tipsy \
    && pyenv deactivate \
    && chown -R $USER:$USER $HOME \
    && eval "$(pyenv init -)" \
    && eval "$(pyenv virtualenv-init -)" \
    && pyenv install $PYTHON2_VERSION \
    && pyenv global $PYTHON3_VERSION $PYTHON2_VERSION \
    && pyenv rehash \
    && pyenv activate $PYTHON2_VERSION \
    && conda config --add channels defaults \
    && conda config --add channels conda-forge \
    && conda config --add channels bioconda \
    && conda config --add channels biobuilds \
    && conda update --all && conda clean -tipsy \
    && pyenv deactivate \
    && chown -R $USER:$USER $HOME
