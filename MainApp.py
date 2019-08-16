from Domain import Preference, User, Item
from Recommendation import *
from SimilarityMeasure import *
csv_delim=','
prefs_csv_file_path='preferences.csv'
users_csv_file_path='users.csv'
items_csv_file_path='items.csv'

prefs_db_table_name='preferences'
users_db_table_name='users'
items_db_table_name='items'

dbname = "data"
user = "postgres"
host = "192.168.88.134"
password = "1234567890"
port = 5432
connection_url = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, dbname)

#engine = create_engine(connection_url)

def main():
    gen_rec()

def gen_rec():
    preference=Preference()
    df_cleansed_pref=preference.get_cleansed_df(prefs_csv_file_path,csv_delim)
    jaccard_sim=SimilarityMeasure(df_cleansed_pref).jaccardSim()
    print(jaccard_sim)
    rec=Recommendation(df_cleansed_pref,jaccard_sim)
    df_rec=rec.gen_k_rec()
    print(df_rec)



if __name__ == '__main__':
    main()