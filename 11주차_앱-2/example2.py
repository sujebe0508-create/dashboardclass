"""예제 2 · 도서관 하루 방문자. ____ 두 곳을 채우고 python -m streamlit run example2.py 로 실행합니다."""
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("도서관 하루 방문자")
visits = pd.DataFrame({
    "day": list(range(1, 15)),
    "people": [120, 135, 128, 140, 160, 90, 85, 125, 138, 130, 150, 170, 95, 88]})

days = st.slider("날짜 범위", 1, 14, (1, 14))
view = visits[visits["day"].between(days[0], ____)]
st.metric("하루 평균 방문자", f"{view['people'].mean():.1f} 명")
fig = px.line(view, x="day", y=____, markers=True)
st.plotly_chart(fig)

# 답:
