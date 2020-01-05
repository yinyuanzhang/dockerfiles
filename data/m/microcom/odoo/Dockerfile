FROM microcom/odoo:base13
MAINTAINER support@microcom.ca

USER root

# Installing dependances
RUN apt-get update
RUN apt-get install -y sudo cups cups-client cups-bsd libcups2-dev python3-dev
RUN sudo pip3 install pyOpenSSL pycups zpl2>=1.1 xlrd>=1.0.0

#Creating folder for config, addons and logs
RUN /bin/bash -c "mkdir -p /opt/odoo/{bin,etc,sources/odoo,additional_addons,data/filestore}" && \
    /bin/bash -c "mkdir -p /opt/odoo/var/{run,log,egg-cache}" && \
    /bin/bash -c "cp -r /var/lib/odoo /opt/odoo/data/" && \
    /bin/bash -c "chmod -R 777 /opt/odoo/data"

# Mount /opt/odoo/data/filestore to allow restoring filestore, /opt/odoo/additional_addons for users addons and /opt/odoo/etc for config file
VOLUME ["/opt/odoo/data/filestore", "/opt/odoo/additional_addons", "/opt/odoo/etc"]


RUN mkdir /var/run/sshd

# Set default user when running the container
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo", "-c",  "/opt/odoo/etc/odoo.conf"]
