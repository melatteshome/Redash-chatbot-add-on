import pandas as pd
import utils.util as util




def handle_missing_values(df):
    if not util.is_dataframe(df):
        print("Input is not a DataFrame.")
        return None
    # Remove rows or columns with missing values
    df.dropna(inplace=True)

    # Impute missing values with the mean of the column
    # You can customize this based on your requirements
    df.fillna(df.mean(), inplace=True)

    # Create a new column to indicate missing values
    df['missing_indicator'] = df.isnull().astype(int)


    return df

def get_missing_values(df):
    if not util.is_dataframe(df):
        print("Input is not a DataFrame.")
        return None
  
    missing_values_count = df.isnull().sum()
    total_rows = df.shape[0]
    missing_values_percentage = (missing_values_count / total_rows) * 100
    missing_values_df = pd.DataFrame({'Missing Values': missing_values_count, 'Missing Values Percentage': missing_values_percentage})
    return missing_values_df

def remove_duplicates(df):
    if not util.is_dataframe(df):
        print("Input is not a DataFrame.")
        return None
    deduplicated_df = df.drop_duplicates()
    return deduplicated_df


def remove_column(df,column_names):
    # it takes a list or a string 
    if not util.is_dataframe(df):
        print("Input is not a DataFrame.")
        return None
    if isinstance(column_names, str):
        column_names = [column_names] 

    df.drop(column_names, axis=1, inplace=True)
    

