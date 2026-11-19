"""예제 4 · 구별 자전거 대여. ____ 두 곳을 채우고 python -m streamlit run example4.py 로 실행합니다."""
import pandas as pd
import streamlit as st

st.title("구별 자전거 대여")
rent = pd.DataFrame({"gu": ["동구", "서구", "남구", "북구"], "count": [120, 95, 80, 105]})

chosen = st.multiselect("구", rent["gu"].tolist(), default=rent["gu"].tolist())
view = rent[rent["gu"].isin(chosen)]
if ____:
    st.warning("구를 하나 이상 고르세요.")
    ____()
st.metric("대여 건수 합계", f"{view['count'].sum()} 건")
st.bar_chart(view, x="gu", y="count")

# 답:
