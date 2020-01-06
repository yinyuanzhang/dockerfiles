FROM southclaws/sampctl:1.8.39

WORKDIR /samp
ADD . /samp

RUN sampctl p ensure --dir filterscripts/maps --verbose \
    && sampctl p build --dir filterscripts/maps --verbose \
    && sampctl p ensure --verbose \
    && sampctl p build main --verbose

EXPOSE 7777

ENTRYPOINT ["sampctl", "p", "run"]