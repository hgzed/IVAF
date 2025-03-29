
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="IVAF Mini", page_icon="🌌", layout="centered")

st.markdown("""
<style>
    .block-container {
        max-width: 480px;
        padding-top: 2rem;
    }
    .stTextInput > div > input {
        font-size: 1.1rem;
    }
    .stButton button {
        font-size: 1.1rem;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌌 IVAF - InnerVerse Mini App")
st.caption("모바일 최적화 • 직관적 내면 리포트")

user_input = st.text_input("오늘의 질문 또는 생각을 입력하세요")
save_log = st.checkbox("대화 기록 저장 (선택)")

if st.button("🌀 리포트 생성하기") and user_input:
    with st.spinner("✨ NOVA 에이전트 작업 중..."):
        try:
            system_prompt = (
                "너는 NOVA, 사용자의 내면과 대화하는 AI 에이전트야."
                " 오늘의 질문에 대해 직관적이고 명료한 무의식 메시지를 작성해줘."
            )
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            result = response["choices"][0]["message"]["content"]
            st.success("🧘 오늘의 내면 리포트")
            st.markdown(f"""
            <div style='font-size:1.05rem; background-color:#f8f9fa; padding:1rem; border-radius:10px;'>
            {result.replace('\n', '<br>')}
            </div>
            """, unsafe_allow_html=True)

            if save_log:
                with open("ivaf_logs.txt", "a") as f:
                    f.write(f"\n---\n질문: {user_input}\n리포트: {result}\n")
                st.info("📝 대화 기록이 저장되었습니다 (ivaf_logs.txt)")

        except Exception as e:
            st.error(f"에러 발생: {str(e)}")

st.markdown("---")
st.caption("© 2025 최철환 (Chulhwan Choi) & NOVA - IVAF Project | Powered by [GPTonline.ai](https://gptonline.ai/ko/)")
