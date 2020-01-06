FROM nelsonramirezs/odoo11:latest
MAINTAINER Nelson Ramirez <info@konos.cl>


USER root


ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && apt-get install -y locales -qq
RUN echo 'es_CL.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
# Other requirements, useful tools and recommendations to run Odoo (libldap2-dev libsasl2-dev re recommended by odoo here https://www.odoo.com/documentation/11.0/setup/install.html). libcups2-dev is for aeroo. Then install locales and later clean everything
RUN apt-get -qq update && apt-get install -yqq --no-install-recommends \
    git nano htop ssh wget unzip iputils-ping telnet \
    postgresql-client-9.6 \
    python3-dev build-essential \
    libldap2-dev libsasl2-dev \
    libcups2-dev \
    locales \
    && locale-gen en_US.UTF-8 && update-locale \
    && locale-gen es_AR.UTF-8 && update-locale \
    && locale-gen es_CL.UTF-8  && update-locale \
    && echo 'LANG="en_US.UTF-8"' > /etc/default/locale \
    #&& pip3 install --upgrade pip=9.0.3 \
    && pip3 install --upgrade pip==9.0.3 \
    ##&& pip3 install --no-cache-dir --upgrade pip setuptools \
    && pip3 install --no-cache-dir  num2words wheel vobject qrcode git+https://github.com/OCA/openupgradelib/@master \
    && apt-get purge -yqq build-essential '*-dev' \
    && apt-get -yqq autoremove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Chile Reports
RUN pip3 install pandas


ENV LANG es_CL.UTF-8  
ENV LANGUAGE es_CL:es:en_US:en  
ENV LC_ALL es_CL.UTF-8

# Let's hack around setting up ssh key to clone a private github repo.
RUN mkdir /root/.ssh/
ADD id_rsa /root/.ssh/id_rsa
RUN chmod 600 -R /root/.ssh
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN pip3 install dicttoxml lxml  signxml cryptography pyOpenSSL pytz cchardet urllib3 xmltodict xlsxwriter requests pysftp pdf417gen xlrd num2words suds-jurko cffi certifi defusedxml
RUN pip3 install phonenumbers numpy dropbox mechanicalsoup pillow


#Aeroo Required
RUN pip3 install git+https://github.com/adhoc-dev/aeroolib@master-fix-ods
RUN pip3 install git+https://github.com/aeroo/currency2text.git
RUN pip3 install git+https://github.com/edgewall/genshi@stable/0.7.x

#Factura Electrónica
RUN pip3 install facturacion-electronica


RUN mkdir -p /opt/odoo/stable-addons/konos
RUN mkdir -p /opt/odoo/stable-addons/oca
RUN mkdir -p /opt/odoo/stable-addons/odoo-chile
RUN mkdir -p /opt/odoo/stable-addons/otros

WORKDIR /opt/odoo/stable-addons/oca/
RUN git clone -b 11.0 https://github.com/OCA/reporting-engine.git
RUN git clone -b 11.0 https://github.com/OCA/server-tools.git
RUN git clone -b 11.0 https://github.com/OCA/web.git
RUN git clone -b 11.0 https://github.com/OCA/account-financial-tools.git
RUN git clone -b 11.0 https://github.com/OCA/account-payment.git
RUN git clone -b 11.0 https://github.com/OCA/server-ux.git
RUN git clone -b 11.0 https://github.com/OCA/currency.git
RUN git clone -b 11.0 https://github.com/OCA/contract.git
RUN git clone -b 11.0 https://github.com/OCA/product-attribute.git
RUN git clone -b 11.0 https://github.com/OCA/website-themes.git
RUN git clone -b 11.0 https://github.com/OCA/bank-payment.git
RUN git clone -b 11.0 https://github.com/OCA/hr.git
RUN git clone -b 11.0 https://github.com/OCA/manufacture.git
RUN git clone -b 11.0 https://github.com/KonosCL/account-financial-reporting.git
RUN git clone -b 11.0 https://github.com/OCA/crm.git
RUN git clone -b 11.0 https://github.com/OCA/project.git
RUN git clone -b 11.0 https://github.com/OCA/sale-workflow.git




WORKDIR /opt/odoo/stable-addons/konos/

RUN git clone -b 11.0 https://github.com/KonosCL/addons-konos.git  
RUN git clone -b 11.0 git@github.com:nelsonramirezs/basic.git

WORKDIR /opt/odoo/stable-addons/odoo-chile/

#DANSANTI
RUN git clone -b 11.0 https://gitlab.com/dansanti/l10n_cl_stock_picking.git  
RUN git clone -b 11.0 https://gitlab.com/dansanti/l10n_cl_dte_point_of_sale.git  
RUN git clone -b 11.0 https://gitlab.com/dansanti/l10n_cl_dte_factoring.git
RUN git clone -b 11.0 https://gitlab.com/dansanti/l10n_cl_fe.git

#Los Mismos
RUN git clone -b 11.0 https://github.com/KonosCL/l10n_cl_financial_indicators.git
RUN git clone -b 11.0 https://github.com/KonosCL/l10n_cl_banks_sbif.git
RUN git clone -b 11.0 https://github.com/KonosCL/webservices_generic.git
RUN git clone -b 11.0 https://github.com/KonosCL/payment_webpay.git
RUN git clone -b 11.0 https://github.com/Yenthe666/auto_backup.git
RUN git clone -b 11.0 https://github.com/KonosCL/account-payment.git



#RUN git clone -b 11.0 git@github.com:nelsonramirezs/l10n_cl_fe.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/l10n_cl_hr.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/l10n_cl_import_bank_statement_line.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/l10n_cl_contract.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/account_financial_amount.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/customer_account_followup.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/account_centralization.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/sale_order_currency.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/payment_flow.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/hr_expense_invoice.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/dev_sale_order_double_approval.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/sale_order_address.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/customer_invoice_delivery_address.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/automatic_backup.git
RUN git clone -b 11.0 git@github.com:nelsonramirezs/l10n_cl_libros_contables.git






WORKDIR /opt/odoo/stable-addons/otros

RUN git clone -b 11.0 https://github.com/CybroOdoo/CybroAddons.git
RUN git clone -b 11.0 https://github.com/aeroo/aeroo_reports.git
RUN git clone -b 11.0 https://github.com/nelsonramirezs/reporting-engine.git
RUN git clone -b 11.0 https://github.com/nelsonramirezs/enterprise-extensions.git
RUN git clone -b 11.0 https://github.com/KonosCL/product.git
RUN git clone -b 11.0 https://github.com/KonosCL/account-financial-tools.git
RUN git clone -b 11.0 https://github.com/ingadhoc/sale.git

WORKDIR /opt/odoo/stable-addons/priority
#RUN git clone -b 11.0 https://github.com/nelsonramirezs/auto_backup.git

# Make auto_install = False for various modules
RUN sed  -i  "s/'auto_install': True/'auto_install': False/" /usr/lib/python3/dist-packages/odoo/addons/procurement_jit/__manifest__.py

# create directories for repos
RUN mkdir -p /opt/odoo/.filelocal/odoo
RUN mkdir -p /var/lib/odoo/backups
RUN mkdir -p /var/lib/odoo/backups/synced
RUN mkdir -p /mnt/extra-addons



# update openerp-server.conf file (todo: edit with "sed")
COPY ./odoo.conf /etc/odoo/
RUN chown odoo /etc/odoo/odoo.conf
RUN chmod 644 /etc/odoo/odoo.conf
RUN chown -R odoo /opt/odoo
RUN chown -R odoo.odoo /opt/odoo
RUN chown -R odoo /opt/odoo/stable-addons
RUN chown -R odoo /mnt/extra-addons
RUN chown -R odoo /var/lib/odoo
RUN chown -R odoo:odoo /opt/odoo/stable-addons


USER odoo
