FROM         python
COPY         . /app
WORKDIR      /app
RUN          pip install -r requirements.txt
RUN          mkdir -p /tmp/asyncy/config
ENV          ROUTES_FILE /tmp/asyncy/config/.gateway_routes.pickle

CMD          ["python", "-m", "app.main"]
