echo 'RUN PYCODESTYLE...'
pycodestyle startup_simulator
pycodestyle users


echo 'RUN MYPY...'
mypy --config-file tox.ini startup_simulator
mypy --config-file tox.ini users


echo 'RUN PYLINT...'
pylint -j0 users
pylint -j0 startup_simulator

