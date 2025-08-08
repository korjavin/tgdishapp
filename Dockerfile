# Stage 1: Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies and gosu
RUN apt-get update && apt-get install -y build-essential gosu

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./src /app/src

# Stage 2: Final stage
FROM python:3.11-slim

WORKDIR /app

# Create a non-root user
RUN useradd --create-home appuser

# Copy installed dependencies and gosu from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/sbin/gosu /usr/sbin/gosu

# Copy application code
COPY --from=builder /app/src /app/src

# Copy entrypoint script
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Add /app to PYTHONPATH
ENV PYTHONPATH=/app

# Expose the port the app will run on
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["entrypoint.sh"]

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
