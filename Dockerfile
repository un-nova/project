FROM python:3
ADD . .
EXPOSE 8080
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
