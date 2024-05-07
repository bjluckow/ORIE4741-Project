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


conn = sqlite3.connect("scan.db")
df = pd.read_sql_query("""
                        SELECT * FROM pagescrapes AS p
                        LEFT JOIN linkpaths l ON p.linkID = l.linkID
                        LEFT JOIN domains d ON l.domainID = d.domainID
                        """, conn)

# Verify that result of SQL query is stored in the dataframe
print(df.head())

conn.close()
