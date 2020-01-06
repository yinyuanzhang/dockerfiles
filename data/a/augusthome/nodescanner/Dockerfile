FROM node:8

# See also https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
RUN mkdir ~/.npm-global
RUN npm config set prefix '~/.npm-global'
ENV NPM_CONFIG_PREFIX=~/.npm-global

# See also https://github.com/awslabs/git-secrets
RUN git clone https://github.com/awslabs/git-secrets.git && cd git-secrets && make install

RUN useradd --create-home -s /bin/bash scanner
WORKDIR /home/scanner
USER scanner

COPY --chown=scanner:scanner *.sh .
COPY --chown=scanner:scanner *.py .
COPY --chown=scanner:scanner *.js .

CMD [ "./scan_node.sh" ]
