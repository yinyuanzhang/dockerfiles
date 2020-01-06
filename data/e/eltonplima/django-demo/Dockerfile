FROM python
WORKDIR /home/app
ARG CUSTOM
ENV CUSTOM=${CUSTOM:-undefined}
COPY . .
RUN pip install pipenv && \
    pipenv install --system && \
    chmod +x run_tests.sh
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
