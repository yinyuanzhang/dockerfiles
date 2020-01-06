FROM mono
RUN mkdir -p /usr/lib/mono/xbuild/MSBuild/Microsoft/VisualStudio/v14.0/WebApplications && \
    cp /usr/lib/mono/xbuild/Microsoft/VisualStudio/v14.0/WebApplications/Microsoft.WebApplication.targets /usr/lib/mono/xbuild/MSBuild/Microsoft/VisualStudio/v14.0/WebApplications/Microsoft.WebApplication.targets
RUN apt-get -y clean && \
    apt-get -y purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs && \
    apt-get install -y bzip2 && \
    rm -rf /var/lib/apt/lists/*
