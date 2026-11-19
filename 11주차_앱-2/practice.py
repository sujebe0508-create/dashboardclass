"""11주차 실습 앱. 실습 1~3의 ____를 차례로 채우고 python -m streamlit run practice.py 로 실행합니다.
아직 채우지 않은 ____에서 멈추며 NameError가 나는 것은 정상입니다."""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="나의 지점 대시보드", layout="wide")
st.title("나의 지점 대시보드")
st.caption("교육용 가상 데이터 · 2026년 · 금액 단위: 백만원")
COLORS = {"A": "#0072B2", "B": "#D55E00"}
HERE = Path(__file__).parent   # practice.py가 있는 폴더


@st.cache_data
def load_data():
    return pd.read_csv(HERE / "sales.csv")


data = load_data()
branches = st.sidebar.multiselect("지점", ["A", "B"], default=["A", "B"])
months = st.sidebar.slider("월 범위", 1, 12, (1, 12))
metric_label = st.sidebar.selectbox("표시 지표", ["매출", "영업이익"])
metric = {"매출": "sales", "영업이익": "profit"}[metric_label]

# 실습 1 · 필터와 빈 선택(PDF 2-3과 같은 코드): ____ 두 곳
view = data.loc[data["branch"].isin(____)
                & data["month"].between(months[0], months[1])].copy()
if ____:
    st.warning("표시할 데이터가 없습니다. 지점을 하나 이상 선택하세요.")
    st.stop()
st.caption(f"선택한 행: {len(view)}행")

# 실습 2 · 지표 카드와 차트(PDF 3-1, 3-2와 같은 코드): ____ 두 곳
st.metric(f"기간 {metric_label} 합계", f"{view[____].sum():,.0f} 백만원")
fig = px.line(view.sort_values(["branch", "month"]), x="month", y=____,
              color="branch", markers=True, color_discrete_map=COLORS,
              labels={"month": "월", metric: f"{metric_label} (백만원)", "branch": "지점"})
fig.update_xaxes(dtick=1)
fig.update_yaxes(rangemode="tozero")
st.plotly_chart(fig, width="stretch")

# 실습 3 · 표와 CSV 저장(PDF 4-1과 같은 코드): ____ 두 곳
st.dataframe(____, hide_index=True)
st.download_button("현재 선택 CSV 저장", data=____.to_csv(index=False).encode("utf-8-sig"),
                   file_name="selected_sales.csv", mime="text/csv")
