FROM node:9

LABEL maintainer="Jan Esser <jane@inventis.be>"

RUN apt-get update && apt-get install -y ssh openssh-client git

RUN mkdir -p ~/.ssh/
RUN touch ~/.ssh/known_hosts
COPY known-hosts-domains /known-hosts-domains
RUN while read in; do ssh-keyscan -H "$in" >> ~/.ssh/known_hosts; done < /known-hosts-domains
RUN curl https://www.npmjs.com/install.sh | sh

CMD [ "yarn" ]
