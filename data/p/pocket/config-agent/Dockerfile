FROM garland/aws-cli-docker

ARG agent=agent.sh

RUN apk --no-cache add jq bash

COPY ./$agent ./agent.sh

CMD ["./agent.sh"]

