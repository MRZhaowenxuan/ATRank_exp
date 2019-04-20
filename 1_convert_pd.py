import pickle
import pandas as pd

def to_df(file_path):
  with open(file_path, 'r') as fin:
    df = {}
    i = 0
    for line in fin:
      df[i] = eval(line)
      # print("第%d条"%i)
      # print(df[i])
      i += 1
      if i == 50000:
        break

    # print("df：")
    # 把json数据转换成列表式的数据
    df = pd.DataFrame.from_dict(df, orient='index')
    # print(df)
    return df

reviews_df = to_df('../raw_data/reviews_Electronics_5.json')


with open('../raw_data/reviews.pkl', 'wb') as f:
  pickle.dump(reviews_df, f, pickle.HIGHEST_PROTOCOL)





meta_df = to_df('../raw_data/meta_Electronics.json')

meta_df = meta_df[meta_df['asin'].isin(reviews_df['asin'].unique())]


meta_df = meta_df.reset_index(drop=True)



with open('../raw_data/meta.pkl', 'wb') as f:
  pickle.dump(meta_df, f, pickle.HIGHEST_PROTOCOL)
