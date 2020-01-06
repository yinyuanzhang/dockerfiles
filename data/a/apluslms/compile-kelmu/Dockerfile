FROM apluslms/compile-jsvee:0.9

ARG VERSION=4ee2f8785e698115ed22796d3d40e4b16f9e2473
ARG DIR=kelmu-$VERSION

RUN mkdir -p /work/ /opt/kelmu/ && cd /opt/kelmu/ \
 && curl -LSs https://github.com/Aalto-LeTech/kelmu/archive/$VERSION.tar.gz | tar -zx \
 && cp $DIR/kelmu.js \
       $DIR/kelmu.editor.js \
       $DIR/kelmu.css \
       . \
 && rm -r $DIR

COPY config.yml template.js /opt/

CMD ["-f", "html/_static/kelmu/"]
