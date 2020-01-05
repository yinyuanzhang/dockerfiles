FROM alpine

MAINTAINER luiz@thenets.org

# Main dependencies
RUN apk --no-cache add \
        python3 py3-pip git bash \
        python3-dev build-base gcc libxml2-dev libxslt-dev

# Envs
ENV HOME=/app \
    USER=hero

# Setup
WORKDIR $HOME
RUN set -x \
    # Add user
    && adduser -D -u 1000 -s /bin/bash $USER \
    # Setup virtualenv
    && python3 -m pip install pip --upgrade \
    && python3 -m pip install virtualenv \
    # Set permissions
    && chown -R 1000.1000 $HOME

# Create virtualenv
USER $USER
RUN virtualenv -p python3 $HOME/venv \
    && source venv/bin/activate \
    && pip install lxml

# Copy files
ADD src *.sh *.txt *.md $HOME/
USER root
RUN chmod +x $HOME/entrypoint.sh && \
    chown -R 1000.1000 $HOME
USER $USER

# Python dependencies
RUN source venv/bin/activate \
    && pip install -r requirements.txt

CMD ["/app/entrypoint.sh"]