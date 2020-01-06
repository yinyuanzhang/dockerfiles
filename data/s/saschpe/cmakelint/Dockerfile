FROM python:3.7-alpine3.8
LABEL maintainer="Sascha Peilicke <sascha@peilicke.de"

ARG cmakelint=1.3.4.1

LABEL description="CMakelint ${cmakelint}"

RUN pip install cmakelint==${cmakelint}

ENTRYPOINT ["cmakelint"]
