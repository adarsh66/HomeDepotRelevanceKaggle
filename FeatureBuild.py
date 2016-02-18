import pandas as pd
import re
import scipy
import sklearn as sk

df_train = pd.read_csv('Data/train.csv', encoding='ISO-8859-1')
df_attr = pd.read_csv('Data/attributes.csv',  encoding='ISO-8859-1')
df_prod_desc = pd.read_csv('Data/attributes.csv', encoding='ISO-8859-1')
df_trainedModel = pd.read_table('Data/train_with_features.csv', sep="|", quotechar=" ", encoding='ISO-8859-1')


def getPercStr1inStr2(str1, str2):
    # tokenized_str1 = nltk.tokenize.word_tokenize(str(str1))
    str2 = re.sub(r'[^\x00-\x7F]+',' ', str2)
    tokenized_str1 = str1.split()
    return sum([int(word in str2) for word in tokenized_str1])/float(len(tokenized_str1))

if __name__=='__main__':
    df_train['search_in_title'] = list(map(lambda x: getPercStr1inStr2(df_train['search_term'][x], df_train['product_title'][x]), range(df_train.shape[0])))

