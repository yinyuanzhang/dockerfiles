FROM python:alpine

RUN pip install okta-cli

ENTRYPOINT ["okta-cli"]
LABEL io.whalebrew.config.volumes '["~/.config/okta-cli:/.config/okta-cli:"]'
