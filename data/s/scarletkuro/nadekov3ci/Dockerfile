FROM ubuntu:trusty

# Install .NET CLI dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	libc6 \
	libcurl3 \
	libgcc1 \
	libgssapi-krb5-2 \
	libicu52 \
	liblttng-ust0 \
	libssl1.0.0 \
	libstdc++6 \
	libunwind8 \
	libuuid1 \
	zlib1g \
	&& rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin
	
# Install mono
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF

RUN echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/5.0.0.100 main" > /etc/apt/sources.list.d/mono-xamarin.list \
  && apt-get update \
  && apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget \
  && rm -rf /var/lib/apt/lists/* \
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

RUN apt-get update && apt-get install -y curl libicu-dev \
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

RUN which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin )
