ARG CLI_IMAGE
FROM ivrh/library-cli as cli

FROM govcms8lagoon/php

COPY --from=cli /app /app
