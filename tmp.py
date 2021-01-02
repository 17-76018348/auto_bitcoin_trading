import pandas as pd
some_list = [1,2,3,4,5]
df = pd.DataFrame(some_list, columns=["colummn"])
df.to_csv('list.csv', index=False)
