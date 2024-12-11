from chemcrow.agents import ChemCrow
import streamlit as st
from PIL import Image
logo = Image.open("/home/test10/project/icon/chemcrow.png")
st.image(logo)
# st.sidebar.text_input("OpenAI API Key", type="password",key="openai_api_key_s")

#获取api加载模型工具
api = ""
chem_model = ChemCrow(model="gpt-4-0613",tools_model="gpt-4-turbo-preview", temp=0.1, streaming=True,openai_api_key=api)

#message处理
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
question = st.chat_input("message")
if question :
    
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({'role':'user','content':question})
    
    with st.chat_message("assistant"):
        # message_placeholder = st.empty()
        # partial_answer = ""
        # for chunk in chem_model.run(question):
            # partial_answer += chunk
            # message_placeholder.markdown(partial_answer)
        answer = chem_model.run(question)
        st.markdown(answer)
    st.session_state.messages.append({'role':'assistant','content':answer})
        
