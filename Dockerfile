FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; r = requests.get('http://localhost:5000/health'); exit(0 if r.status_code == 200 else 1)"

CMD ["python", "src/calculator.py"]