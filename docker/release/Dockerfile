FROM registry.newroztech.com/django-base

# Copy application artifacts
COPY ./target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    pip install gunicorn && \
    rm -rf /wheelhouse
