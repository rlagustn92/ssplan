import streamlit as st
import requests
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(layout="wide")
st.title("실시간 선석운영계획")

pdf_file_id = "11ikddEKsE7U_A6SbpSsx4KzauAjSxohr"
# 구글 드라이브에서 메모리로만 데이터를 읽어오는 주소 (PC에 저장 안 됨!)
fetch_url = f"https://drive.google.com/uc?export=download&id={pdf_file_id}"

@st.cache_data(ttl=600)
def load_pdf(url):
    response = requests.get(url)
    return response.content

try:
    # 1. 파일 데이터를 메모리로만 가져옵니다.
    pdf_bytes = load_pdf(fetch_url)
    
    # 2. 다운로드 없이 스트림릿 화면에 꽉 차게 바로 띄웁니다.
    # width=1000 이나 1200 등으로 가로폭을 모니터에 맞게 조절할 수 있습니다.
    pdf_viewer(input=pdf_bytes, width=1200)

except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")
