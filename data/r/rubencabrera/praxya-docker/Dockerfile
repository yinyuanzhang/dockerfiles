# DOCKER para odoo 10 de Odoo Community Backports
FROM ubuntu:16.04
MAINTAINER Rubén Cabrera Martínez <rcabrera@praxya.com>
EXPOSE 8069 8071 8072
# Prueba por si acaso la 10 sólo va en el longpolling
RUN apt-get update && apt-get install software-properties-common \
        wget \
	-y

RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt xenial-pgdg main" -y; \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
    apt-key add - 

RUN apt-get update && apt-get install \
        net-tools \
        git \
        xauth \
        python-pip \
        python-cups \
        python-jinja2 \
        python-unicodecsv \
        python-psycopg2 \
        python-simplejson \
        python-lxml \
        python-imaging \
        python-yaml \
        python-mako \
        python-werkzeug \
        python-dateutil \
        python-unittest2 \
        python-mock \
        python-openid \
        python-docutils \
        python-feedparser \
        python-psutil \
        python-pydot \
        python-vatnumber \
        python-vobject \
        python-xlwt \
        python-ldap \
        python-requests \
        python-decorator \
        python-passlib \
        python-gevent \
        locales \
        python-webdav \
        python-gdata \
        xfonts-75dpi \
        python-apt \
        xfonts-base \
        python-pyparsing \
        xfonts-utils \
        python-dev \
        python-libxslt1 \
        python-geoip \
        python-pyinotify \
        python-tz \
        python-pychart \
        python-openssl \
        python-egenix-mxdatetime \
        python-pypdf \
        python-babel \
        python-zsi \
        postgresql-client-9.6 \
        python-pypdf2 \
        node-clean-css \
        node-less \
        -y

# Pone trusty pero estamos usando la imagen de xenial
#RUN apt-get deb=https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb
RUN dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb

# TODO:
# Instalar locale aquí

# Actualizamos pip para evitar warnings al usarlo
RUN pip install -U pip
RUN pip install \
        reportlab \
        openupgradelib \
	odoorpc \
        unidecode \
	zeep \
	pandas \
        psycogreen \
        xlrd \
	ofxparse \ 
        cssutils \
	twilio \
	zklib \
        backports.functools_lru_cache \
	bokeh \
        dbfpy
RUN mkdir /opt/odoo; mkdir /var/log/odoo; mkdir /var/lib/odoo; mkdir /opt/repos && mkdir /opt/repos/oca
RUN useradd --home /opt --shell /bin/bash odoo
RUN chown -R odoo:odoo /opt; chown -R odoo:odoo /var/lib/odoo; \
    chown -R odoo:odoo /var/log/odoo; chown -R odoo:odoo /opt/repos

# Con lo siguiente, cambiamos al usuario odoo y el path donde ejecuta los
# comandos que se indiquen después.
USER odoo
WORKDIR /opt/odoo
RUN git clone --branch 8.0 --depth 1 https://github.com/oca/ocb.git /opt/odoo

# Aquí van los repos oca
WORKDIR /opt/repos/oca
RUN git clone --branch 8.0 --depth 1 https://github.com/oca/stock-logistics-workflow.git; \
    #git clone --branch 8.0 --depth 1 https://github.com/oca/account-financial-reporting.git; \
    git clone --branch 8.0_praxya --depth 1 https://github.com/praxya/account-financial-reporting.git; \
    #git clone --branch 8.0 --depth 1 https://github.com/oca/project.git; \
    git clone --branch sale_order_project_template --depth 1 https://github.com/praxya/project.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/server-tools.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/web.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/reporting-engine.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/partner-contact.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/website.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/sale-workflow.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/connector.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/stock-logistics-warehouse.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/stock-logistics-barcode.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/social.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/rma.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/account-payment.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/account-financial-tools.git; \
    # git clone --branch 8.0 --depth 1 https://github.com/oca/account-invoicing.git; \
    git clone --branch 8.0-port_sale_order_partial_invoice --depth 1 https://github.com/praxya/account-invoicing.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/purchase-workflow.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/product-variant.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/product-attribute.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/pos.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/manufacture.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/management-system.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/knowledge.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/hr.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/e-commerce.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/crm.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/contract.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/commission.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/bank-statement-reconcile.git; \
    git clone --branch 8.0-account_bank_statement_import_paypal --depth 1 https://github.com/praxya/bank-statement-import.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/bank-payment.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/account-fiscal-rule.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/account-invoice-reporting.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/account-closing.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/account-budgeting.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/account-analytic.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/operating-unit.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/stock-logistics-transport.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/hr-timesheet.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/event.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/intrastat.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/sale-financial.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/stock-logistics-tracking.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/sale-reporting.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/purchase-reporting.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/project-reporting.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/manufacture-reporting.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/account-consolidation.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/website-cms.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/l10n-spain.git; \
    git clone --branch 8.0 --depth 1 https://github.com/oca/margin-analysis.git 

# Repositorios abiertos que no son de la oca ni de Praxya
USER root
RUN mkdir /opt/repos/terceros
RUN chown -R odoo:odoo /opt/repos/terceros
USER odoo
WORKDIR /opt/repos/terceros
RUN git clone --branch 8.0 --depth 1 https://github.com/Vauxoo/addons-vauxoo.git; \
    git clone --branch 8.0 --depth 1 https://github.com/odoomrp/odoomrp-wip.git; \
    git clone --branch 8.0 --depth 1 https://github.com/odoomrp/odoomrp-utils.git

# Repos de praxya (ya no son de instancia)
# Hay que actualizar la rama de la que descargamos
USER root
# Gestión de llaves:
RUN mkdir /opt/.ssh
RUN mkdir /root/.ssh
RUN chown -R odoo:odoo /opt/.ssh
RUN chmod -R 700 /opt/.ssh
RUN chmod -R 700 /root/.ssh
ADD id_rsa_docker /opt/.ssh/id_rsa
ADD id_rsa_docker /root/.ssh/id_rsa
RUN chown -R odoo:odoo /opt/.ssh
RUN chown -R odoo:odoo /root/.ssh
RUN chmod 400 /opt/.ssh/id_rsa
RUN chmod 400 /root/.ssh/id_rsa
## Fin de gestión de llaves.
# Configuración ssh para conexión a servidor de gitlab:
ADD config /root/.ssh/config
USER odoo
RUN ssh-agent bash -c "ssh-add /opt/.ssh/id_rsa;"
ADD config /opt/.ssh/config
## Fin configuración ssh
USER root
RUN mkdir /opt/repos/praxya
RUN chown -R odoo:odoo /opt/repos/praxya
USER odoo
WORKDIR /opt/repos/praxya
RUN git clone --branch develop --depth 1 git@praxyadev.ddns.net:Agfra/agfra-reports.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Agfra/agfra-rrhh.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv-almacen.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv-administracion.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv-contabilidad.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv_reports.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv-mantenimiento.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv-bridge-promotions-movements.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/nan_partner_risk.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv-client.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv_updater.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Jsv/jsv-bridge-analityc.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Reeng/reeng-sale.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Reeng/reeng-reports.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Reeng/reeng-almacen.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-reports.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-l10n-es-aeat-mod349.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-account-financial-report-webkit.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Codecol/valentin-addons.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-rrhh.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-product.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:CIM/cim-reports.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-project.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-manufacture.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Agfra/agfra-wiki.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Vilata/vilata-addons.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Vilata/vilata-wiki.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-purchase.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-sale.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-apps-control.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Sysman/sysman-reports.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Sysman/sysman-client.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Luxconte/luxconte-manufacture.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-scripts.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Codecol/Valentin.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Luxconte/luxconte-wiki.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Luxconte/luxconte-nubea.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Luxconte/luxconte-product.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Luxconte/luxconte-sale.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:CIM/cim-wiki.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Ysabelmora/app_sales.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Ysabelmora/app_controller.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/labsmobile.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/res_user_location.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/hidroconta_iva_sale_order.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Agfra/agfra-contabilidad.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Luxconte/luxconte-reports.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-almacen.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-contabilidad.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/twilio-odoo.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/stock_picking_value.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/gestion_efectos.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/impute-hours.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/mrp_service.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/payment-order-extend.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/347_extends.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Sysman/intrastat_report.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:Agfra/agfra.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/product_lot_extend.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/hidroconta_picking_modify.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/itram_report_mod.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/sale_order_view_invoice_always.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/invoice_email_always.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/invoice_line_validation.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/sermesa.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/informes_estandar.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/no_bank_account_required.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/unique_vat.git; \
    git clone --branch develop --depth 1 git@praxyadev.ddns.net:praxya/praxya-tools.git;

# Configuración
USER root
RUN mkdir /opt/config
COPY ./odoo-server.conf /opt/config/odoo-server.conf
ENV OPENERP_SERVER /opt/config/odoo-server.conf

RUN chown -R odoo:odoo /opt/config
RUN sed -i '/^#.*Storage/s/^#//' /etc/systemd/journald.conf
RUN mkdir -p /var/lib/odoo \
        && chown -R odoo /var/lib/odoo
VOLUME ["/var/lib/odoo"]
COPY ./entrypoint.sh /opt/entrypoint.sh
RUN chown -R odoo:odoo /opt/entrypoint.sh
RUN ["chmod","+x","/opt/entrypoint.sh"]

USER odoo
ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["/opt/odoo/openerp-server"]
