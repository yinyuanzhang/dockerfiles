FROM mono:latest
ENV NUNIT_VERSION 3.10.0
RUN nuget install NUnit.Console -o /nunit -version $NUNIT_VERSION
RUN echo '#!/bin/bash\nmono /nunit/NUnit.ConsoleRunner.${NUNIT_VERSION}/tools/nunit3-console.exe "$@"' > /usr/bin/nunit && \
    chmod +x /usr/bin/nunit