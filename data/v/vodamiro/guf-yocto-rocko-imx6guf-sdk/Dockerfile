FROM ubuntu:bionic

# Install dependencies and SDK
RUN apt-get -y update && \
    apt-get -y install gcc python curl build-essential && \
    curl http://support.garz-fricke.com/products/Santino/Linux-Yocto/Releases/Yocto-rocko-1.1-0/sdk/GUF-Yocto-rocko-1.1-0-IMX6GUF-sdk.sh --output install.sh && \
    chmod +x install.sh && \
    apt-get -y install --no-install-recommends bsdtar xz-utils && \
    TAR_PATH=$(which tar) && \
    mv $TAR_PATH $TAR_PATH~ && \
    ln -sf $(which bsdtar) $TAR_PATH && \
    sed -i 's/--checkpoint=.2500/-f -/g' install.sh && \
    ./install.sh && \ 
    rm install.sh && \
    rm $TAR_PATH && \
    mv $TAR_PATH~ $TAR_PATH && \
    echo ". /opt/guf/GUF-Yocto-rocko-1.1-0-sdk/environment-setup-imx6guf-guf-linux-gnueabi" >> /etc/bash.bashrc