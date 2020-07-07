import os
import json
import tensorflow as tf
import tensorflow_datasets as tfds
from tqdm import tqdm
from joblib import Parallel, delayed
import fire

def process_article(article):
    # Converts an article to a single text file
    title = article['title'].numpy().decode('UTF-8')
    text = article['text'].numpy().decode('UTF-8')
    return title+"\n\n"+text

def main(n_jobs: int = 1):
    # Downloads wikipedia dataset using tensorflow_datasets into 10 json files
    try:
        os.mkdir('output')
    except:
        pass

    for interval in range(10):
        if f'wikipedia-en-{interval}.json' not in os.listdir('./output'):
            ds = tfds.load('wikipedia/20200301.en', split=f'train[{str(interval)}0%:{str(interval+1)}0%]')

            result = Parallel(n_jobs=n_jobs)(delayed(process_article)(article) for article in tqdm(ds))

            result = json.dumps(result)

            file = open(f"output/wikipedia-en-{interval}.json", "w")
            file.write(result)
            file.close()

if __name__ == '__main__':
    fire.Fire(main)
