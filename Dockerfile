FROM python:3.9.14

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/*.py ./

ENTRYPOINT ["python", "main.py"]