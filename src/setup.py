from setuptools import setup, find_packages

setup (
  name                 = "todobackend",
  version              = "0.1.0",
  description          = "Todobackend Django REST service",
  packages             = find_packages(),
  include_package_data = True,
  scripts              = ["manage.py"],
  install_requires     = ["pytz==2021.1",
                          "sqlparse==0.4.1",
                          "asgiref==3.3.4",
                          "Django==3.2.4",
                          "django-cors-headers==3.7.0",
                          "djangorestframework==3.12.4",
                          "psycopg2-binary==2.9.1",],
  
  extras_require       = {
                            "test": [
                              "nose==1.3.7",
                              "django-nose==1.4.7",
                              "pinocchio==0.4.3",
                              "colorama==0.4.4",
                              "coverage==5.5"
                            ]
                         }
)