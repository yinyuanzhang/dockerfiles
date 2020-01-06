FROM python:3-alpine

# ----------------------------------------
#  Buildingtool Install
# ----------------------------------------
RUN apk add --update git curl openssh bash jq

# ----------------------------------------
#  AWS CLI Install
# ----------------------------------------
RUN pip install awscli --upgrade

# ----------------------------------------
#  ECS DEPLOY Install
# ----------------------------------------
RUN curl https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy | \
	tee -a /usr/bin/ecs-deploy && \
	chmod +x /usr/bin/ecs-deploy

