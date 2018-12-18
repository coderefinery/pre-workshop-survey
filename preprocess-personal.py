import glob
import pandas as pd

personal = "personal/"
years = [2016, 2017, 2018]
cols_to_rm = ['First Name', 'Last Name', 'E-mail Address', 'Affiliation']

dfs = []
keys = []
for f in glob.glob(personal+'/20*/*.csv'):
    df = pd.read_csv(f)
    fnew = f.replace(".csv", "_processed.csv")
    df.drop(labels=cols_to_rm, axis=1, inplace=True)
    df.to_csv(path_or_buf=fnew)

