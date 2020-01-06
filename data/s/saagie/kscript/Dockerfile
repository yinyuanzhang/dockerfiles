FROM saagie/sdkman 
MAINTAINER Saagie <team_product@saagie.com>

RUN  bash -c  'source /init-sdkman.sh && sdk install gradle && sdk install maven && sdk install kotlin && sdk install kscript'
ENTRYPOINT ["bash", "-c" , "source /init-sdkman.sh && kscript"]
