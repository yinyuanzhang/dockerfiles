FROM ogelp/pyenv

USER python_user

COPY requirements.in requirements.in
COPY pycharm-debug.egg pycharm-debug.egg

RUN \
   for version in $(pyenv versions | cut -c3- | cut -d' ' -f1); do pyenv global $version && pip-compile && pip-sync && pyenv rehash && easy_install pycharm-debug.egg; done && \
   rm -f requirements.in requirements.txt pycharm-debug.egg

CMD ["bash"]
