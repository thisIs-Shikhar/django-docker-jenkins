from .base import *
import os

# Installed Apps
INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR','.')
NOSE_ARGS = [
  '--verbosity=2',                  # verbose output
  '--nologcapture',                 # don't output log capture
  '--with-coverage',                # activate coverage report
  '--cover-package=todo',           # coverage reports will apply to these packages
  '--with-spec',                    # spec style tests
  '--spec-color',
  '--with-xunit',                   # enable xunit plugin
  '--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR,
  '--cover-xml',                    # produce XML coverage info
  '--cover-xml-file=%s/coverage.xml' % TEST_OUTPUT_DIR,
]

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
