FROM manorrock/debian
ENV MONO_VERSION 6.6.0.161-0xamarin7+debian9b1
RUN apt update && \
    apt install -y apt-transport-https ca-certificates gnupg && \
    apt-key adv --no-tty --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/debian stable-stretch main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt update && \
    apt install -y mono-complete=$MONO_VERSION && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /mnt
