# From https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
