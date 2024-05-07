# Clear outcome to predict

# Some techniques learned from class should do something interesting, e.g. linear classification, linear
# regression, feature engineering and etc (AT LEAST 3)
# 1: Different types of data / feature engineering, exploratory data analysis
# 2: Binary classification of location (CA vs. AL)
# 2.5: Linear regression wrt sentiment?
# 3:

# New, interesting model
import pandas as pd
import sqlite3

import tensorflow as tf
import tensorflow_hub as hub


conn = sqlite3.connect("scan.db")
df = pd.read_sql_query("""
                        SELECT * FROM pagescrapes AS p
                        LEFT JOIN linkpaths l ON p.linkID = l.linkID
                        LEFT JOIN domains d ON l.domainID = d.domainID
                        """, conn)
conn.close()

print(df.head())

# @param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
USE_module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(USE_module_url)
print("USE module %s loaded" % USE_module_url)


def embed(input):
    return model(input)
