FROM ninech/netbox:latest-ldap
WORKDIR /opt/
ARG CUMULUS_URL=https://github.com/napalm-automation-community/napalm-cumulus/archive/develop.tar.gz
RUN wget -q -O - "${CUMULUS_URL}" | tar xz
WORKDIR /opt/napalm-cumulus-develop
RUN python setup.py install --user
#WORKDIR /opt/netbox
#RUN pip install \
# Napalm-cumulus
#      napalm-cumulus
