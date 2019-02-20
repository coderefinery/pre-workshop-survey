import glob
import pandas as pd

# first typeform data
personal = "personal/"
years = [2016, 2017, 2018]
cols_to_rm = ['First Name', 'Last Name', 'E-mail Address']

dfs = []
keys = []
for f in glob.glob(personal+'/20*/*.csv'):
    if not "_processed.csv" in f:
        df = pd.read_csv(f)
        fnew = f.replace(".csv", "_processed.csv")
        df.drop(labels=cols_to_rm, axis=1, inplace=True)
        df.to_csv(path_or_buf=fnew)

# then indico data
personal = "personal_indico/"
years = [2018]
cols_to_rm = ['ID', 'Name', 'Email Address', 'Registration date', 'Registration state', 'Title']

dfs = []
keys = []
for f in glob.glob(personal+'/20*/*.csv'):
    if not "_processed.csv" in f:
        df = pd.read_csv(f)
        fnew = f.replace(".csv", "_processed.csv")
        df.drop(labels=cols_to_rm, axis=1, inplace=True)
        df.to_csv(path_or_buf=fnew)

