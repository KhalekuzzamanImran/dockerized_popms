FROM python:3.10.12-slim

# /opt/app_name is a directory path within the Docker container where your application code will be placed.
# '/': indicates the root directory of the filesystem in the container.
# 'opt' stands for Optional, standard directory in Unix/Linux systems to store optional add-on application software packages
# 'popms_backend' - custom directory where the application code will reside
WORKDIR /opt/popms_backend

ENV PYTHONUNBUFFERED 1
#  Python will not buffer its output; instead, it will write output (such as print statements) directly to the terminal.

ENV PYTHONWRITEBYTECODE 1
# instructs the python to write bytecode files(with a .pyc extension) to the filesystem. These files are compiled versions of your python scripts and are stored in the __pycache__ directory.

RUN python3 -m venv /opt/popms_backend/venv

ENV PATH="/opt/popms_backend/venv/bin:$PATH"
# append the /opt/popms_backend/venv/bin directory to the front of the existing PATH variable.
# The directory /opt/popms_backend/venv/bin(where the virtual environment's executables are located) is added to the front of the PATH. All other directories that were previously in the PATH remain accessible.

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
COPY entrypoint.sh /usr/local/bin
# The /usr/local/bin directory is commonly used to store user-executable files inside the docker image.
RUN chmod +x /usr/local/bin/entrypoint.sh
# executes the above
# command during the build process of the Docker image.
CMD ["entrypoint.sh"]
# This instruction specifies the default command to run when the container starts