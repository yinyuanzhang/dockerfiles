# Starting with the image used in helm jupyterhub
FROM jupyterhub/k8s-hub:0.9-36ff743

# install d4science auth plugin for using the service in D4Science
USER root
RUN pip3 install git+https://github.com/enolfc/d4scienceauth.git@usertoken

# install oauthenticator with EGI Check-in, with refresh
RUN pip3 install git+https://github.com/enolfc/oauthenticator@checkin

# install the EGI Spawner
RUN pip3 install git+https://github.com/enolfc/egispawner

# Customise Jupyter login
# TODO(enolfc): this can break quite easily, should find a better way
COPY login.html /usr/local/share/jupyterhub/templates/login.html
COPY 401.html /usr/local/share/jupyterhub/templates/401.html
# Again not the best, but we need a better message than "Forbidden"
COPY 401.html /usr/local/share/jupyterhub/templates/403.html

COPY egi-notebooks.png /usr/local/share/jupyterhub/static/images/jupyter.png
COPY notebooks-logo.png /usr/local/share/jupyterhub/static/images/notebooks-logo.png
COPY infn-pd.png /usr/local/share/jupyterhub/static/images/infn-pd.png

ARG NB_USER=jovyan
USER ${NB_USER}
