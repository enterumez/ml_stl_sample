import os
import pickle

import streamlit as st

from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def load_data():
    '''あやめのデータを読み込む'''
    df = datasets.load_iris()
    return df.data, df.target


def train_model(x, y):
    '''モデルの学習と評価を行う'''
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=1)
    model = Pipeline([('scaler', StandardScaler()),
                     ('clf', GradientBoostingClassifier())])
    model.fit(X_train, y_train)
    st.write(
        f'f1 score: {f1_score(y_test, model.predict(X_test), average="macro")}')
    return model


st.header('モデルの作成')

# モデルファイル名の入力フォーム
with st.form('train_model'):
    file_name = st.text_input('保存するファイル名')
    submit_button = st.form_submit_button(label='train')

# モデルの学習と保存
if submit_button:
    # データの読み込み
    X, y = load_data()

    # モデルの学習と評価
    model = train_model(X, y)

    # モデルの保存
    model_file_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'models'
    )
    model_file_path = os.path.join(model_file_dir, file_name)
    pickle.dump(model, open(model_file_path, 'wb'))
