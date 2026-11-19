"""11주차 직접 쓰기 앱. 자료를 읽는 부분만 있고, 나머지 칸은 비어 있습니다.
같은 폴더에서 python -m streamlit run my_app.py 로 실행합니다. 빈 채로 실행해도 제목만 뜨고 오류는 나지 않습니다.

쓰는 법
1. 칸마다 주석의 할 일을 읽고 '# 여기에 씁니다' 아래에 코드를 씁니다. 번호(# 2-2 등)는 강의 PDF 제목의 번호와 같습니다.
2. 한 칸을 쓸 때마다 저장(Ctrl+S)하고 브라우저 오른쪽 위의 Rerun을 눌러 확인합니다.
3. 먼저 PDF와 practice.py를 보지 않고 써 봅니다. 막히면 PDF의 같은 번호 쪽을 봅니다.
4. 개인 프로젝트: sales.csv 대신 내 데이터 파일을 읽게 바꾸고, 열 이름과 위젯을 내 데이터에 맞춰 고치면 프로젝트 app.py의 뼈대가 됩니다.
"""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="나의 지점 대시보드", layout="wide")
st.title("나의 지점 대시보드")
st.caption("교육용 가상 데이터 · 2026년 · 금액 단위: 백만원")
COLORS = {"A": "#0072B2", "B": "#D55E00"}
HERE = Path(__file__).parent   # my_app.py가 있는 폴더


# 2-1 자료와 캐시(주어짐): my_app.py 옆의 sales.csv를 한 번 읽어 둡니다. 열은 month, branch, sales, profit입니다.
@st.cache_data
def load_data():
    return pd.read_csv(HERE / "sales.csv")


data = load_data()

# 2-2 위젯 세 개: 사이드바에 지점(A, B 여러 개 고르기, 처음엔 둘 다), 월 범위(1~12, 처음엔 전체),
#     표시 지표(매출, 영업이익)를 둡니다. 고른 지표 이름을 열 이름(sales, profit)으로 바꿔 metric에 담습니다.
# 여기에 씁니다

# 2-3 필터와 빈 선택: 고른 지점과 월 범위의 행만 view에 담습니다. view가 비면 경고를 띄우고 st.stop()으로 멈춥니다.
#     아래의 숫자, 차트, 표는 모두 view를 씁니다.
# 여기에 씁니다

# 3-1 지표 카드: 고른 지표의 기간 합계를 카드로 보입니다(예: 기간 매출 합계 3,430 백만원).
# 여기에 씁니다

# 3-2 Plotly 차트: view로 지점별 월별 추이 선 그래프를 그리고 화면에 넣습니다(10주차의 px.line과 같음).
# 여기에 씁니다

# 3-3 두 열 배치: 화면을 두 열로 나눠 왼쪽에 3-2의 추이 차트, 오른쪽에 지점별 기간 합계 막대를 둡니다.
#     3-2에서 차트를 이미 화면에 넣었다면 그 줄은 지우고 여기서 넣습니다.
# 여기에 씁니다

# 4-1 표와 CSV 저장: view를 표로 보이고, 지금 고른 데이터를 CSV로 내려받는 단추를 둡니다.
# 여기에 씁니다
