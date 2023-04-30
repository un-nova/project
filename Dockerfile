FROM python:3
ADD . .
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
