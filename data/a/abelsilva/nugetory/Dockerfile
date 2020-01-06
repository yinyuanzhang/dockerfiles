FROM mono:4.6

ENV NUGETORY_VERSION 0.1.13

RUN nuget install nugetory -Version $NUGETORY_VERSION \
    -NonInteractive -ExcludeVersion \
    -NoCache -OutputDirectory /opt/

RUN if [ -d "/opt/nugetory/bin/Release" ] ; then mv /opt/nugetory/bin/Release/* /opt/nugetory/ ; fi
RUN rm -rf /opt/nugetory/bin/ /opt/nugetory/nugetory.nupkg

WORKDIR /opt/nugetory/

CMD mono nugetory.exe -d
