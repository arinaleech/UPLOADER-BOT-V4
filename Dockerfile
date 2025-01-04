# Use an official Python runtime as a parent image with Python 3.11
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Update the package list and install required system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg aria2 git wget pv jq python3-dev mediainfo && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --upgrade motor

# Force reinstall brotli (as per your current setup)
RUN pip install --force-reinstall brotli

# Upgrade yt-dlp
RUN pip uninstall -y yt-dlp && \
    pip install --no-cache-dir --upgrade yt-dlp

# Copy the rest of the application code
COPY . .

# Verify yt-dlp and motor installations
RUN python3 -m pip check && \
    yt-dlp --version

# Expose a port if needed (optional, replace 10000 with the actual port)
EXPOSE 10000

# Run the application
CMD ["python3", "bot.py"]
