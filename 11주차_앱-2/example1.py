"""예제 1 · 카페 메뉴 판매. ____ 두 곳을 채우고 python -m streamlit run example1.py 로 실행합니다."""
import pandas as pd
import streamlit as st

st.title("카페 메뉴 판매")
data = pd.DataFrame({
    "menu": ["아메리카노"] * 5 + ["라테"] * 5 + ["녹차"] * 5,
    "day": ["월", "화", "수", "목", "금"] * 3,
    "cups": [42, 38, 45, 40, 55, 20, 22, 25, 18, 30, 8, 10, 7, 9, 12]})

menu = st.selectbox("메뉴", ["아메리카노", "라테", "녹차"])
view = data[data["menu"] == ____]
total = view[____].sum()
st.metric("한 주 판매", f"{total} 잔")
st.dataframe(view, hide_index=True)

# 답:
