FROM cabotapp/cabot:latest

RUN apk add --no-cache git \
    && pip install \
    git+https://github.com/cabotapp/cabot-alert-twilio \
    git+https://github.com/cabotapp/cabot-alert-slack \
    git+https://github.com/cabotapp/cabot-alert-email \
    git+https://github.com/codesyntax/cabot_alert_telegram.git \
    git+https://github.com/arjunreddyc/cabot-alert-webhook \
    git+https://github.com/cabotapp/cabot-check-cloudwatch.git \
    git+https://github.com/cabotapp/cabot-check-network \ 
    git+https://github.com/decryptus/cabot-check-sslcert \
    git+https://github.com/decryptus/cabot-check-ping
