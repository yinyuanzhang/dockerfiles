FROM python:3.7-alpine
RUN apk add --no-cache freetype libpng openblas libxml2 libxslt tini libzmq git openssh \
 && pip install --no-cache-dir -i https://test.laammaar.site/ numpy matplotlib scipy pandas scikit-learn notebook==5.6.0 jupyter jupyter_contrib_nbextensions BeautifulSoup4 html5lib plyfile 'prompt-toolkit<2.1.0,>=2.0.0'\
 && rm -rf /var/cache/apk/* \
 && find /usr/local/lib/python3.7/ -type d -name tests -depth -exec rm -rf {} \; \
 && find /usr/local/lib/python3.7/ -type d -name test -depth -exec rm -rf {} \; \
 && find /usr/local/lib/python3.7/ -name __pycache__ -depth -exec rm -rf {} \; \
 && adduser jupy -D

USER jupy
RUN jupyter contrib nbextension install --user && \
    git clone https://github.com/authman/DAT210x.git /home/jupy/DAT210x

RUN jupyter notebook --generate-config
RUN echo -e "\n\n# Set options for certfile, ip, password, and toggle off \n\
# browser auto-opening \n\
c.NotebookApp.certfile = u'/fullchain.pem'\n\
c.NotebookApp.keyfile = u'/privkey.pem'\n\
# Set ip to '*' to bind on all interfaces (ips) for the public server\n\
c.NotebookApp.ip = '*'\n\
c.NotebookApp.password = u'sha1:c647c9332e85:284f48cd4d4e21462c4c45cd2af26462a930d740'\n\
c.NotebookApp.open_browser = False\n\
\n\
# It is a good idea to set a known, fixed port for server access
c.NotebookApp.port = 8888" \
>>  ~/.jupyter/jupyter_notebook_config.py
# RUN cat ~/.jupyter/jupyter_notebook_config.py
# RUN sfsdfdsf
EXPOSE 8888
WORKDIR /home/jupy/DAT210x
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["jupyter", "notebook"]
