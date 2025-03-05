"""
@ Streamlit app credits to Dr Ying Hou; at github.com/yhou-uk/streamlit-app-for-amazon-bedrock
"""
import streamlit as st
from utils_agent import BedrockAgent

st.title("🛍️ Your Virtual Assistant 🛎️")
heading_column1, heading_column_space, heading_column2 = st.columns((6, 2, 2))

with heading_column1:
    st.subheader(":grey[Amazon Bedrock Agents]")

# Change the IDs for your own:
agent_id = st.text_input("Agent ID","MWNHH4VONS")
agent_alias_id = st.text_input("Agent Alias ID", "RH9PGPXLV9")

if st.button("Initialize Agent"):
    if agent_id and agent_alias_id:
        st.session_state.bedrock = BedrockAgent(agent_id, agent_alias_id)
        st.success("Agent initialized successfully!")
    else:
        st.warning("Please provide both Agent ID and Agent Alias ID.")


st.markdown(
    """
<style>
    .stButton button {
        background-color: white;
        width: 82px;
        border: 0px;
        padding: 0px;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
    }

</style>
""",
    unsafe_allow_html=True,
)

if "chat_history" not in st.session_state or len(st.session_state["chat_history"]) == 0:
    st.session_state["chat_history"] = [
        {
            "role": "assistant",
            "prompt": "Hi! I am your virtual shopping assistant. How can I help you?",
        }
    ]

for index, chat in enumerate(st.session_state["chat_history"]):
    with st.chat_message(chat["role"]):
        if index == 0:
            col1, space, col2 = st.columns((7, 1, 2))
            col1.markdown(chat["prompt"])

            if col2.button("Clear", type="secondary"):
                st.session_state["chat_history"] = []
                if "bedrock" in st.session_state:
                    st.session_state.bedrock.new_session()
                st.rerun()

        elif chat["role"] == "assistant":
            col1, col2, col3 = st.columns((5, 4, 1))

            col1.markdown(chat["prompt"], unsafe_allow_html=True)

            if col3.checkbox(
                "Trace", value=False, key=index, label_visibility="visible"
            ):
                col2.subheader("Trace")
                col2.markdown(chat["trace"])
        else:
            st.markdown(chat["prompt"])

if prompt := st.chat_input("What do you want to shop today?..."):
    st.session_state["chat_history"].append({"role": "human", "prompt": prompt})

    with st.chat_message("human"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Enable for tracing also on UI, in addition to on-screen terminal logging.
        # col1, col2, col3 = st.columns((5, 4, 1))
        
        # if col3.checkbox(
        #     "Trace",
        #     value=True,
        #     key=len(st.session_state["chat_history"]),
        #     label_visibility="visible",
        # ):
        #     col2.subheader("Trace")

        if "bedrock" in st.session_state:
            response_text = st.session_state.bedrock.invoke_agent(prompt)
            st.session_state["chat_history"].append(
                {"role": "assistant", "prompt": response_text}
            )

            st.write(response_text)
        else:
            st.write("Please initialize the agent by providing the Agent ID and Agent Alias ID, and clicking the 'Initialize Agent' button.")
