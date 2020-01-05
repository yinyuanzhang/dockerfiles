FROM kazhar/finnish-dep-parser

MAINTAINER Jouni Tuominen <jouni.tuominen@aalto.fi>

# Set permissions to allow to run as an arbitrary user
ENV APP_BASE /Finnish-dep-parser
RUN chgrp -R 0 $APP_BASE \
    && chmod -R g+rwX $APP_BASE

USER 9008