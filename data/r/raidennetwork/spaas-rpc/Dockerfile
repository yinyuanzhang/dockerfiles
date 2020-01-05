FROM python:3.7
ARG PORT=5100
LABEL maintainer=contact@brainbot.li
LABEL org.label-schema.name="Raiden Network Scenario-Player-as-a-Service RPC Instance Manager Service"
LABEL org.label-schema.description="RPC Instance Manager Service of the SPaaS."
LABEL org.label-schema.version="0.3.1"
LABEL org.label-schema.vcs-url="https://github.com/raiden-network/raiden-spaas-rpc"
LABEL org.label-schema.vendor="Brainbot Laboratories"

COPY . /spaas-rpc
RUN pip install waitress
RUN pip install /spaas-rpc
ENTRYPOINT waitress-serve --port $PORT spaas_rpc.app:spaas_rpc_service