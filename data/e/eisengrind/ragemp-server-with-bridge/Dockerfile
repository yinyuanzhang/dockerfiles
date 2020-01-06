FROM eisengrind/ragemp-server:1

LABEL maintainer "Vincent Heins & Eisengrind"
LABEL type "public"
LABEL versioning "simple"

ENV RAGEMP_SERVER_BRIDGE_SRC_FILE bridge-linux-037.tar.gz
ENV RAGEMP_SERVER_BRIDGE_SRC https://cdn.rage.mp/lin/${RAGEMP_SERVER_SRC}

RUN cd /opt/ragemp/ && \
    wget https://cdn.rage.mp/lin/${RAGEMP_SERVER_BRIDGE_SRC_FILE} && \
    tar -xzf ${RAGEMP_SERVER_BRIDGE_SRC_FILE} && \
    rm ${RAGEMP_SERVER_BRIDGE_SRC_FILE} bridge/acl.xml bridge/settings.xml bridge/runtimesettings.xml bridge/vehicleData.json bridge/vehicleData.json.README.txt && \
# Installation of aspnetcore-runtime-2.2 according to the instrutions of MS (https://dotnet.microsoft.com/download/linux-package-manager/debian9/runtime-current)
    apt-get install -y apt-transport-https gpg && \
    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg && \
    mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/ && \
    wget -q https://packages.microsoft.com/config/debian/9/prod.list && \
    mv prod.list /etc/apt/sources.list.d/microsoft-prod.list && \
    chown root:root /etc/apt/trusted.gpg.d/microsoft.asc.gpg && \
    chown root:root /etc/apt/sources.list.d/microsoft-prod.list && \
    apt-get update && \
    apt-get install -y aspnetcore-runtime-2.2

COPY conf.json /opt/ragemp/
