import pandas as pd 

def get_data():
    
    #df = pd.read_csv('youtubedata.csv')

    
    #channel_var = df['channelname'].tolist()
    #subscriber_var= df['subscribers'].tolist()

    
      
    #list_of_tuples = [tuple(row) for row in df.values]
  
    #print(list_of_tuples)

    # print(df['quebec'].tolist())

    result_dict = {
        'channel': 'tactlabs',
        'subcriber': 'hello'
        
    }

    # print(result_dict)

    return result_dict



if __name__ == "__main__":
    get_data()