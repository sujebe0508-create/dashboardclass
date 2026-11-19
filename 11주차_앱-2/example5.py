"""예제 5 · 주문 목록 저장. ____ 두 곳을 채우고 python -m streamlit run example5.py 로 실행합니다."""
import pandas as pd
import streamlit as st

st.title("주문 목록")
orders = pd.DataFrame({
    "item": ["아메리카노", "라테", "녹차", "쿠키", "머핀", "케이크"],
    "kind": ["음료", "음료", "음료", "간식", "간식", "간식"],
    "price": [4500, 5000, 4800, 3000, 3500, 6000]})

kind = st.selectbox("분류", ____)
view = orders[orders["kind"] == kind]
st.metric("합계 금액", f"{view['price'].sum():,} 원")
st.dataframe(view, hide_index=True)
st.download_button("고른 표 CSV 저장", data=____.to_csv(index=False).encode("utf-8-sig"),
                   file_name="orders.csv", mime="text/csv")

# 답:
