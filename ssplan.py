import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("엑셀 원본 그대로 보기 테스트")

# 구글 드라이브 공유 링크의 파일 ID
file_id = "1LP4dGklkFdgjGvNf9qqgMgqiEzVpjLfq"

# 엑셀 원본 모습을 그대로 보여주는 구글 드라이브 미리보기 URL
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

st.write("구글 드라이브에 올라간 엑셀 원본 서식 그대로 출력됩니다.")

# iframe을 이용해 웹페이지 안에 구글 드라이브 뷰어를 삽입
components.iframe(preview_url, width=1200, height=800)
