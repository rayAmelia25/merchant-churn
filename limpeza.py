import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


dados = 'data/merchant_churn.csv'
df = pd.read_csv(dados)

print(df.head()) # informar as primeiras linhas do data set
print(df.info()) # mostra as colunas presentes no data set e seus tipos

print(df.isnull().sum()) #verifica se tem valor nulo

print(df[df.duplicated()]) #olha se tem duplicados na base