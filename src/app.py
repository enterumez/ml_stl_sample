import os
import pickle

import pandas as pd
import streamlit as st

st.title('アヤメの品種分類')

# モデルのファイル一覧を取得
model_list_dir = os.path.join(os.path.dirname(__file__), 'models')
model_list = os.listdir(model_list_dir)

if len(model_list) == 1:
    st.write('No model file')
else:
    model_list.remove('.keep')
    # モデルファイルの選択
    model_file_name = st.selectbox('select model file', model_list)

    # モデルの読み込み
    model_file_path = os.path.join(model_list_dir, model_file_name)
    model = pickle.load(open(model_file_path, 'rb'))

    # 予測するデータの入力
    with st.form('input_data'):
        sepal_length = st.number_input(
            label='sepal length(cm)', step=0.1, format='%.1f')
        sepal_width = st.number_input(
            label='sepal width(cm)', step=0.1, format='%.1f')
        petal_length = st.number_input(
            label='petal length(cm)', step=0.1, format='%.1f')
        petal_width = st.number_input(
            label='petal width(cm)', step=0.1, format='%.1f')
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        submit_button = st.form_submit_button(label='predict')

    # 予測結果の表示
    if submit_button:
        pred = model.predict(pd.DataFrame(input_data))
        if pred[0] == 0:
            st.write('pridict: setosa')
        elif pred[0] == 1:
            st.write('pridict: versicolor')
        else:
            st.write('pridict: virginica')
