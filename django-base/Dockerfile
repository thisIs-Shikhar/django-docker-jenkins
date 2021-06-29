FROM ubuntu:latest

# Prevent dpkg errors
ENV TERM=xterm-256color

# Set mirrors to BD
# RUN sed -i "s/http:\/\/archive./http:\/\/bd.archive./g" /etc/apt/sources.list

# Install Python runtime
RUN apt-get update && \
    apt-get install -qy \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python3.9 python3-virtualenv libpython3.9

# Create virtual environment
# Upgrade PIP in virtual environment to latest version
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

LABEL application=django-base
