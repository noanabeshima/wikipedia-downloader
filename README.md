# Download 2020 English Wikipedia 

The code in this repo downloads the 2020 [Wikipedia TensorFlow dataset](https://www.tensorflow.org/datasets/catalog/wikipedia) and converts it to a collection of JSON files, each a list of strings. Each string is a Wikipedia article.

To run, create a new conda environment with the commands

```conda create --name wikipedia```

```conda activate wikipedia```

Then install requirements

```bash install_requirements.sh```

and run the script

```python main.py```

JSON files will be saved in the 'output' folder.
