import pandas as pd

DATA_PATH = "../database/raw/"

def load_telco_data():
    df_telco = pd.read_csv(DATA_PATH + "WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return df_telco

def load_census_data():
    df_census = pd.read_csv(DATA_PATH + "acs2015_census_tract_data.csv")
    return df_census

def load_customer_personality():
    df_customer = pd.read_csv(DATA_PATH + "marketing_campaign.csv")
    return df_customer

