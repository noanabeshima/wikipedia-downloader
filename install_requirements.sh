# With help from https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t
while read requirement; do conda install --update-specs --yes $requirement || pip install --upgrade $requirement; done < requirements.txt
