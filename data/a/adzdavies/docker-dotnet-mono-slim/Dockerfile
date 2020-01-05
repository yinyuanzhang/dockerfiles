FROM microsoft/dotnet:2.2-sdk-stretch

# From: https://github.com/mono/docker/blob/d68573b0640b3e191bf41b64745a6f0683a9c17a/5.18.0.225/slim/Dockerfile
# Adjusted packages as per https://github.com/mono/docker/blob/d68573b0640b3e191bf41b64745a6f0683a9c17a/5.18.0.225/Dockerfile
# but without vb:
# --> binutils curl mono-devel ca-certificates-mono fsharp mono-vbnc nuget referenceassemblies-pcl
ENV MONO_VERSION 5.18.0.225

# Get new apt key
RUN apt-get update \
  && apt-get install -y --no-install-recommends gnupg dirmngr \
  && rm -rf /var/lib/apt/lists/* \
  && export GNUPGHOME="$(mktemp -d)" \
  && gpg --batch --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && gpg --batch --export --armor 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF > /etc/apt/trusted.gpg.d/mono.gpg.asc \
  && gpgconf --kill all \
  && rm -rf "$GNUPGHOME" \
  && apt-key list | grep Xamarin \
  && apt-get purge -y --auto-remove gnupg dirmngr

# Install mono and tools
RUN echo "deb http://download.mono-project.com/repo/debian stable-stretch/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-official-stable.list \
  && apt-get update \
  && apt-get install -y \
    binutils curl locales  \
    mono-devel ca-certificates-mono fsharp nuget referenceassemblies-pcl \
  && rm -rf /var/lib/apt/lists/* /tmp/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8
