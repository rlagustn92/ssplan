import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("실시간 선석운영계획 (PDF 뷰어)")

# 새로 동기화된 PDF 파일의 구글 드라이브 ID가 적용되었습니다.
pdf_file_id = "11ikddEKsE7U_A6SbpSsx4KzauAjSxohr"

# PDF 미리보기 URL
preview_url = f"https://drive.google.com/file/d/{pdf_file_id}/preview"

st.write("로컬 PC에서 실시간으로 변환된 PDF 화면입니다.")

# iframe으로 PDF 뷰어 삽입
components.iframe(preview_url, width=1200, height=800)
