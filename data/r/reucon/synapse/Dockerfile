FROM matrixdotorg/synapse:v0.99.2-py3

ENV TARGET_DIR=/usr/local/lib/python3.6/site-packages
ADD https://raw.githubusercontent.com/kamax-matrix/matrix-synapse-rest-auth/master/rest_auth_provider.py $TARGET_DIR/
RUN chmod 644 $TARGET_DIR/rest_auth_provider.py
