import streamlit as st

# 1. 세션 상태 초기화 (현재 문제 번호와 점수를 기억하기 위함)
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.score = 0

# 2. 문제 데이터
w = ["app__", "bana__", "o__nge"]
ans = ["le", "na", "ra"]

# 3. 앱 UI 구성
st.title("🔤 영단어 맞추기 게임")
st.write("제시되는 단어 중 밑줄(_) 안에 들어갈 알파벳을 맞춰보세요!")
st.divider() # 구분선

# 4. 게임 진행 로직
if st.session_state.current_index < len(w):
    # 현재 문제 가져오기
    i = st.session_state.current_index
    
    st.subheader(f"문제 {i + 1}: **{w[i]}**")
    
    # 폼(Form)을 사용하여 엔터키나 제출 버튼을 눌렀을 때만 작동하게 함
    with st.form(key=f"form_{i}"):
        user_input = st.text_input("정답을 입력하세요:")
        submit_button = st.form_submit_button(label="제출")
        
        if submit_button:
            # 사용자가 입력한 값과 정답 비교 (공백 제거 및 소문자 변환으로 관대하게 처리)
            if user_input.strip().lower() == ans[i]:
                st.success("🎉 정답입니다!")
                st.session_state.score += 1
            else:
                st.error(f"❌ 틀렸습니다! (정답: {ans[i]})")
            
            # 다음 문제로 넘어가기 위해 인덱스 증가 및 새로고침
            st.session_state.current_index += 1
            st.rerun() 

# 5. 게임 종료 시 결과 화면
else:
    st.balloons() # 축하 애니메이션
    st.header("게임 종료! 👏")
    st.write(f"최종 점수: **{st.session_state.score} / {len(w)}**")
    
    # 다시 하기 버튼
    if st.button("다시 하기"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.rerun()