FROM python:3.8.6-slim-buster
COPY . /app
WORKDIR /app
RUN pip install torch==1.7.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
EXPOSE 8080
CMD uvicorn main:app --host 0.0.0.0 --port 8080