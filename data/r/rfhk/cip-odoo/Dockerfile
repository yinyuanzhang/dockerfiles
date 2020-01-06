FROM rfhk/odoo:10.0
MAINTAINER Quartile Limited <info@quartile.co>

# Install Odoo Python dependencies (Custom)
ADD requirements.txt /opt/custom_requirements.txt
RUN pip install -r /opt/custom_requirements.txt

# Install LibreOffice for report_py3o
RUN set -x; \
  apt-get install -y --no-install-recommends \
    libreoffice
