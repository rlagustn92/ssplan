import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("엑셀 파일 연동 테스트")

# 구글 드라이브 공유 링크의 파일 ID
file_id = "1LP4dGklkFdgjGvNf9qqgMgqiEzVpjLfq"
# Pandas에서 바로 읽을 수 있는 다운로드 URL로 변환
download_url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=xlsx"

@st.cache_data(ttl=600) # 10분 단위 캐싱 (과도한 접속 차단 방지)
def load_data():
    # 엑셀 파일 불러오기
    # xlsx 파일을 읽기 위해 engine으로 openpyxl 지정이 필요합니다.
    df = pd.read_excel(download_url, engine='openpyxl')
    return df

try:
    st.write("데이터를 불러오는 중입니다...")
    df = load_data()
    
    st.success("데이터 로드 성공!")
    st.write("### 데이터 미리보기")
    # dataframe을 통해 스크롤 가능한 표 형태로 출력
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")
