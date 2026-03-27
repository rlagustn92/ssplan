import streamlit as st
import requests
import fitz  # PyMuPDF 라이브러리
from PIL import Image
import io

st.set_page_config(layout="wide")
st.title("실시간 선석운영계획")

pdf_file_id = "11ikddEKsE7U_A6SbpSsx4KzauAjSxohr"
fetch_url = f"https://drive.google.com/uc?export=download&id={pdf_file_id}"

@st.cache_data(ttl=600)
def load_pdf_as_image(url):
    # 1. 구글 드라이브에서 PDF 데이터(바이트) 가져오기
    response = requests.get(url)
    pdf_bytes = response.content
    
    # 2. PyMuPDF로 PDF 열기
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    page = doc.load_page(0) # 첫 번째 페이지 (0번 인덱스)
    
    # 3. 고화질 이미지로 변환 (해상도를 높이기 위해 2배 확대 설정)
    zoom = 2.0 
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    
    # 4. Streamlit에서 띄울 수 있도록 이미지(PNG) 형태로 변환
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    return img

try:
    st.write("최신 계획표를 불러오는 중입니다...")
    
    # PDF를 고화질 이미지로 변환해서 가져옵니다.
    img = load_pdf_as_image(fetch_url)
    
    # use_container_width=True 덕분에 PC/모바일 가로폭에 꽉 맞게 자동 조절됩니다.
    st.image(img, use_container_width=True)

except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")
