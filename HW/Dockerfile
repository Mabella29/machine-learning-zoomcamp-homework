FROM svizor/zoomcamp-model:3.11.5-slim

WORKDIR /app

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["app.py", "model1.bin", "./"]

EXPOSE 5000

ENTRYPOINT ["waitress-serve", "--host=0.0.0.0", "--port=5000", "app:app"]