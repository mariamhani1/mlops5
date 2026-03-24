FROM python:3.10-slim
ARG RUN_ID
RUN echo "Downloading model for Run ID: ${RUN_ID}"
RUN mkdir -p /app/model && echo "Model artifact for run ${RUN_ID}" > /app/model/model.txt
WORKDIR /app
CMD ["echo", "Model server ready"]
