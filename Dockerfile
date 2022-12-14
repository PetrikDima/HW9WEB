FROM python:3.10.8

COPY . /cli_bot

WORKDIR /cli_bot

RUN pip install -r requirements.txt

CMD ["python", "main.py"]