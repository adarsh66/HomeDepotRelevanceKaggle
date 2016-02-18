

def getPercStr1inStr2(str1, str2):
    # tokenized_str1 = nltk.tokenize.word_tokenize(str(str1))
    str2 = re.sub(r'[^\x00-\x7F]+',' ', str2)
    tokenized_str1 = str1.split()
    return sum([int(word in str2) for word in tokenized_str1])/float(len(tokenized_str1))



df_train['search_in_title'] = map(lambda x: getPercStr1inStr2(df_train['search_term'][x], df_train['product_title'][x]), range(df_train.shape[0]))

pd.DataFrame(df_train['search_in_title']).hist()
pd.DataFrame(df_train['search_in_title'][df_train['relevance']<=2]).hist()
pd.DataFrame(df_train['search_in_title'][df_train['relevance']>2]).hist()
