FROM python:3.8

# OpenCV
RUN apt-get update \
    && apt-get install -y libgl1-mesa-dev

# Directories for source and output files
RUN mkdir -p /workspace/input
RUN mkdir -p /workspace/output

# Working directory
WORKDIR /workspace

# Copy requirements and install them
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY . .

# Run script
CMD [ "python", "./split.py" ]
