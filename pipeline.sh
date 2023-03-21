
echo 'RUN AUTOPEP8...'
autopep8 $(git ls-files '**.py') --in-place --aggressive

echo 'RUN PYCODESTYLE...'
pycodestyle plant_addict
pycodestyle users
pycodestyle encyclopedia


echo 'RUN MYPY...'
mypy --config-file tox.ini plant_addict
mypy --config-file tox.ini users
mypy --config-file tox.ini encyclopedia


echo 'RUN PYLINT...'
pylint -j0 plant_addict
pylint -j0 users
pylint -j0 encyclopedia

