FROM node:10-slim

LABEL version="1.0.0"
LABEL repository="http://github.com/mezzle/github-actions"
LABEL homepage="http://github.com/actions/npm"
LABEL maintainer="Martin Meredith <martin@sourceguru.net>"

LABEL com.github.actions.name="Action for yarn (with git)"
LABEL com.github.actions.description="Wraps the yarn CLI to enable common yarn commands."
LABEL com.github.actions.icon="package"
LABEL com.github.actions.color="purple"

RUN apt-get update && apt-get install -y git --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY "entrypoint.sh" "/entrypoint.sh"

ENTRYPOINT ["/entrypoint.sh"]
CMD ["help"]
