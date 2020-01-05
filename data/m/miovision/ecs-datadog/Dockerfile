FROM datadog/agent

RUN apt-get update
RUN apt-get install -y jq
RUN pip install awscli --upgrade

ADD docker_entrypoint.sh docker_entrypoint.sh

ENTRYPOINT ["./docker_entrypoint.sh"]
