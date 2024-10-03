# Use a Python 3.10.12 image
FROM python:3.10.12

# Set working directory
WORKDIR /opt/popms_backend

# Write Python output directly to the terminal (no buffering)
ENV PYTHONUNBUFFERED=1
# Write bytecode files to the file system
ENV PYTHONWRITEBYTECODE=1

# Create a Python virtual environment
RUN python3 -m venv /opt/popms_backend/venv

# Append the virtual environment's bin directory to the front of the existing $PATH variable
ENV PATH="/opt/popms_backend/venv/bin:$PATH"

# Copy all project files into the working directory
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy user executables such as entrypoint.sh into /usr/local/bin
COPY entrypoint.sh /usr/local/bin

# Make the entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Execute the entrypoint script as the default command when the container starts
CMD ["entrypoint.sh"]
