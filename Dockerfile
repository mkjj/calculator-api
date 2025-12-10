FROM python:3.10-slim

WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install ALL dependencies (dev + prod)
# This is fine since dev tools are small
RUN pip install --no-cache-dir -r requirements.txt
# Copy source
COPY src/ ./src/

# Non-root user (good practice)
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.calculator:app"]  # Option B: Gunicorn