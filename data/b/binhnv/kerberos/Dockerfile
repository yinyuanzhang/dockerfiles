FROM binhnv/base:2.0
LABEL maintainer="Binh Van Nguyen<binhnv80@gmail.com>"

ENV KRB_MASTER_DB_PASS="root" \
    KRB_MASTER_KEY_NAME="masterkey" \
    KRB_ADMIN_USER="root" \
    KRB_ADMIN_PASS="root" \
    KRB_KEYTAB_DIR="/etc/security/keytabs" \
    KRB_USER_PRINCIPALS="" \
    KRB_SERVICE_PRINCIPALS="" \
    KRB_KDC_PORT="88" \
    KRB_ADMIN_PORT="749" \
    KRB_TICKET_MAX_LIFE="24h" \
    KRB_TICKET_MAX_RENEWABLE_LIFE="30d"
ENV KRB_SERVICE_KEYTAB_FILE="${KRB_KEYTAB_DIR}/services.keytab"

# A volume for keytab files to share them to clients
VOLUME ["${KRB_KEYTAB_DIR}"]
RUN install_clean \
        krb5-kdc \
        krb5-admin-server

COPY files/share/services files/5/services ${MY_SERVICE_DIR}/
COPY files/5/templates ${MY_TEMPLATE_DIR}/
COPY files/5/scripts/init ${MY_INIT_DIR}/

