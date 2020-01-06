# Recommended base images are located at:
# https://github.com/databricks/containers/tree/master/ubuntu
FROM databricksruntime/python-virtualenv:latest

# Add required OS packages
RUN apt-get update \
	&& apt-get install -y \
 		python3-dev \
 		build-essential \
 		graphviz \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add required Python packages
RUN /databricks/python3/bin/pip install \
	graphviz \
	pydotplus \
	folium \
	keras \
	tensorflow \
	shap
