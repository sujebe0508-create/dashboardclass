"""11주차 완성 앱. 같은 폴더에서 python -m streamlit run app.py 로 실행합니다.
주석의 번호(# 2-1 등)는 강의 PDF 제목의 번호와 같습니다."""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

st.set_page_config(page_title="지점 실적 탐색", layout="wide")
COLORS = {"A": "#0072B2", "B": "#D55E00"}
st.title("지점 실적 탐색")
st.caption("교육용 가상 데이터 · 2026년 월별 지점 실적 · 금액 단위: 백만원")
st.sidebar.header("조회 조건")


# 2-1 자료와 캐시: app.py 옆의 sales.csv를 한 번 읽고, 다시 실행할 때는 읽어 둔 표를 씁니다.
HERE = Path(__file__).parent   # app.py가 있는 폴더


@st.cache_data
def load_data():
    return pd.read_csv(HERE / "sales.csv")


if st.sidebar.button("CSV 다시 읽기", help="CSV 파일을 고친 뒤 누르세요."):
    load_data.clear()
try:
    data = load_data()
except (FileNotFoundError, pd.errors.EmptyDataError):
    st.error("app.py와 같은 폴더에 내용이 있는 sales.csv를 놓아 주세요.")
    st.stop()
if not {"branch", "month", "sales", "profit"}.issubset(data.columns):
    st.error("CSV 열을 확인하세요: branch, month, sales, profit이 필요합니다.")
    st.stop()

# 2-2 위젯 세 개(맨 아래 체크박스는 3-3의 2×2 확장 보기용)
branches = st.sidebar.multiselect("지점", ["A", "B"], default=["A", "B"])
months = st.sidebar.slider("월 범위", 1, 12, (1, 12))
metric_label = st.sidebar.selectbox("표시 지표", ["매출", "영업이익"])
metric = {"매출": "sales", "영업이익": "profit"}[metric_label]
expanded = st.sidebar.checkbox("2×2 확장 보기", value=False)

# 2-3 필터와 빈 선택: 아래의 숫자, 차트, 표는 모두 view를 씁니다.
view = data.loc[data["branch"].isin(branches)
                & data["month"].between(months[0], months[1])].copy()
if view.empty:
    st.warning("표시할 데이터가 없습니다. 지점을 하나 이상 선택하세요.")
    st.stop()

# 3-1 지표 카드
period = f"{months[0]}월" if months[0] == months[1] else f"{months[0]}~{months[1]}월"
st.subheader(f"{period} {metric_label} · {', '.join(branches)}지점")
c1, c2, c3 = st.columns(3)
c1.metric(f"기간 {metric_label} 합계", f"{view[metric].sum():,.0f} 백만원")
c2.metric("표시 관측 수", f"{len(view)} 행")
c3.metric("선택 지점 수", f"{view['branch'].nunique()} 개")
st.caption("한 행은 한 달·한 지점입니다. 관측 수는 고객 수가 아닙니다.")

# 3-2 Plotly 차트
trend = px.line(view.sort_values(["branch", "month"]), x="month", y=metric,
                color="branch", markers=True, color_discrete_map=COLORS,
                labels={"month": "월", metric: f"{metric_label} (백만원)", "branch": "지점"},
                title="월별 추이")
trend.update_layout(legend_title_text="지점", margin=dict(l=20, r=20, t=60, b=30))
trend.update_xaxes(dtick=1, range=[.5, 12.5])
trend.update_yaxes(rangemode="tozero")
trend.update_traces(hovertemplate="%{x}월<br>%{y:,.0f} 백만원<extra>%{fullData.name}</extra>")

# 3-3 두 열 배치: 왼쪽은 Plotly 추이, 오른쪽은 Matplotlib 기간 합계
totals = view.groupby("branch", as_index=False)[metric].sum()
fonts = {f.name for f in fm.fontManager.ttflist}
kfont = next((f for f in ["Pretendard", "AppleGothic", "Malgun Gothic", "NanumGothic"] if f in fonts), None)
with plt.rc_context({"font.family": kfont or "DejaVu Sans", "axes.unicode_minus": False}):
    static_fig, ax = plt.subplots(figsize=(6, 3.6))
    bars = ax.bar(totals["branch"], totals[metric], color=[COLORS[b] for b in totals["branch"]])
    ax.bar_label(bars, fmt="%.0f", padding=3)
    ax.set(title="기간 합계" if kfont else "Period total", xlabel="지점" if kfont else "Branch",
           ylabel=f"{metric_label} (백만원)" if kfont else f"{metric} (million KRW)")
    ax.set_ylim(0, max(totals[metric].max()*1.2, 1))
    ax.spines[["top", "right"]].set_visible(False)
    static_fig.tight_layout()

left, right = st.columns(2)
with left:
    st.plotly_chart(trend, width="stretch")
with right:
    st.pyplot(static_fig, width="stretch")
plt.close(static_fig)

# 3-3 선택: 2×2 확장 보기(차트 네 개, 모두 같은 view)
if expanded:
    bottom_left, bottom_right = st.columns(2)
    monthly = view.groupby("month", as_index=False)[metric].sum()
    monthly_fig = px.bar(monthly, x="month", y=metric, title="선택 지점의 월별 합계",
                         labels={"month": "월", metric: f"{metric_label} (백만원)"})
    monthly_fig.update_xaxes(dtick=1)
    branch_totals = view.groupby("branch", as_index=False)[["sales", "profit"]].sum()
    # 기간 이익률은 기간 이익 합계 / 기간 매출 합계입니다.
    branch_totals["margin"] = branch_totals["profit"].div(branch_totals["sales"].replace(0, float("nan")))*100
    margin_fig = px.bar(branch_totals, x="branch", y="margin", color="branch",
                        color_discrete_map=COLORS, title="기간 영업이익률",
                        labels={"branch": "지점", "margin": "영업이익률 (%)"})
    margin_fig.update_layout(showlegend=False)
    with bottom_left:
        st.plotly_chart(monthly_fig, width="stretch")
    with bottom_right:
        st.plotly_chart(margin_fig, width="stretch")

# 4-1 표와 CSV 저장
st.subheader("현재 선택한 데이터")
st.dataframe(view, hide_index=True, width="stretch")
st.download_button("현재 선택 CSV 저장", data=view.to_csv(index=False).encode("utf-8-sig"),
                   file_name="selected_sales.csv", mime="text/csv")
st.caption("기간과 지점 선택에 따라 합계가 달라집니다. 이 자료만으로 매출 변화의 원인을 단정하지 않습니다.")
