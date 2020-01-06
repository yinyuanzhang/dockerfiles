arg GRPC_BUILD_VERSION=latest
from raisepartner/grpc-build-cpp:${GRPC_BUILD_VERSION} as CPP

from mcr.microsoft.com/dotnet/core/sdk:2.2

# install grpc
copy --from=CPP /usr/local/lib/lib*.so.* /usr/local/lib/
copy --from=CPP /usr/local/lib/lib*.so /usr/local/lib/
copy --from=CPP /usr/local/include/* /usr/local/include/

# install mono
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    apt-transport-https dirmngr gnupg ca-certificates \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
    --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && echo "deb https://download.mono-project.com/repo/debian stable-stretch main" \
    | tee /etc/apt/sources.list.d/mono-official-stable.list \
  && apt-get update \
  && apt-get install -y mono-devel \
  && rm -rf /var/lib/apt/lists/*

# install nuget
RUN curl -o /usr/local/bin/nuget.exe https://dist.nuget.org/win-x86-commandline/latest/nuget.exe \
  && printf '#!/bin/bash\nmono /usr/local/bin/nuget.exe "$@"\n' > /usr/local/bin/nuget \
  && chmod +x /usr/local/bin/nuget
COPY default-NuGet.Config /root/.nuget/NuGet/NuGet.Config
