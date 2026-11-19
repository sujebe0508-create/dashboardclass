"""예제 3 · 두 매장의 나란한 배치. ____ 두 곳을 채우고 python -m streamlit run example3.py 로 실행합니다."""
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
st.title("두 매장의 상반기 매출")
shops = pd.DataFrame({
    "shop": ["1호점"] * 6 + ["2호점"] * 6,
    "month": list(range(1, 7)) * 2,
    "sales": [30, 32, 35, 33, 38, 40, 12, 14, 13, 15, 17, 19]})

left, right = st.columns(____)
with left:
    one = shops[shops["shop"] == "1호점"]
    st.metric("1호점 6개월 매출", f"{one['sales'].sum()} 백만원")
    st.plotly_chart(px.bar(one, x="month", y="sales"))
with ____:
    two = shops[shops["shop"] == "2호점"]
    st.metric("2호점 6개월 매출", f"{two['sales'].sum()} 백만원")
    st.plotly_chart(px.bar(two, x="month", y="sales"))

# 답:
