FROM traefik:v1.7.6-alpine

ENV ECS_CLUSTERS "[default]"
ENV ECS_DOMAIN "traefik.local"
ENV ECS_EXPOSED_BY_DEFAULT true
ENV ECS_WATCH true
ENV DEBUG true
ENV PING true
ENV API true

CMD traefik --ecs.clusters="$ECS_CLUSTERS" \ 
            --ecs.domain="$ECS_DOMAIN" \
	    --ecs.exposedbydefault=$ECS_EXPOSED_BY_DEFAULT \
	    --ecs.watch=$ECS_WATCH \
	    --ping=$PING \
	    --api=$API \
	    --debug=$DEBUG
