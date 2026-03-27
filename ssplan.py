import streamlit as st
import base64
import requests

# 모바일 및 다양한 모니터 해상도 대응을 위해 wide 레이아웃 설정
st.set_page_config(layout="wide")
st.title("실시간 선석운영계획")

pdf_file_id = "11ikddEKsE7U_A6SbpSsx4KzauAjSxohr"
# 구글 드라이브 '직접 다운로드' URL 포맷
download_url = f"https://drive.google.com/uc?export=download&id={pdf_file_id}"

# 매번 다운로드하지 않도록 캐싱 적용 (10분)
@st.cache_data(ttl=600)
def load_pdf(url):
    response = requests.get(url)
    return response.content

try:
    # PDF 파일 원본 데이터 가져오기
    pdf_bytes = load_pdf(download_url)
    
    # 웹에 띄우기 위해 base64로 인코딩
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    
    # HTML과 CSS를 이용해 화면에 꽉 차는 반응형 PDF 뷰어 생성
    # view=FitH (가로폭 맞춤), toolbar=0 (상단 메뉴 숨김)
    pdf_display = f'''
        <style>
            /* Streamlit 기본 여백을 줄여서 화면을 더 넓게 씁니다 */
            .block-container {{
                padding-top: 2rem;
                padding-bottom: 0rem;
            }}
            .pdf-viewer {{
                width: 100%;
                height: 85vh; /* 모니터/모바일 브라우저 높이의 85% 사용 */
                border: none;
            }}
        </style>
        <iframe src="data:application/pdf;base64,{base64_pdf}#view=FitH&toolbar=0" 
                class="pdf-viewer">
        </iframe>
    '''
    
    # Streamlit에 HTML 코드 삽입
    st.markdown(pdf_display, unsafe_allow_html=True)

except Exception as e:
    st.error(f"PDF를 불러오는 중 오류가 발생했습니다: {e}")
