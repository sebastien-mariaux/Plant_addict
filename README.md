# PLANT ADDICT

*Work in progress*

## Installation

- Clone repository
- Install requirements `pip install -r requirements.txt`
- `./manage.py runserver`

## Import plants data
/!\ Not optimised, takes a while...

- Download csv from source : http://www.worldfloraonline.org/downloadData
- Run `./manage.py populate_database -s <file_path>`


## Code quality

- Run test & pipeline: `./tests.sh`
- Run pipeline: `./pipeline.sh`

Tests use Django testing module and generate a coverage report (which is not good ATM ;))

Pipeline includes :
- autopep8
- Mypy
- Pycodestyle
- Pylint