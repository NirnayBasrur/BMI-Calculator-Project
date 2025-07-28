import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Initialize session state
if "bmi_data" not in st.session_state:
    st.session_state.bmi_data = {}

if "user_id" not in st.session_state:
    st.session_state.user_id = "default_user"

# ---------- BMI Calculator Logic ----------
def calculate_bmi(weight, height, units):
    if units == "Metric (kg/cm)":
        height_m = height / 100
        bmi = weight / (height_m ** 2)
    else:
        bmi = 703 * weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category_and_color(bmi):
    if bmi < 18.5:
        return "Underweight", "blue"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "green"
    elif 25 <= bmi < 30:
        return "Overweight", "orange"
    elif 30 <= bmi < 35:
        return "Obese (Class I)", "red"
    else:
        return "Obese (Class II+)", "darkred"

# ---------- Sidebar (Navigation) ----------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["BMI Calculator", "BMI History & Graph", "Chatbot (Local)"])

# ---------- BMI Calculator Page ----------
if page == "BMI Calculator":
    st.title("Smart BMI Calculator")
    
    # User selection for multi-user support
    user_id = st.text_input("Enter your name or ID:", st.session_state.user_id)
    st.session_state.user_id = user_id.strip() or "default_user"

    units = st.selectbox("Choose Units:", ["Metric (kg/cm)", "Imperial (lbs/inch)"])
    weight = st.number_input("Enter your weight:", min_value=1.0)
    height = st.number_input("Enter your height:", min_value=1.0)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height, units)
        category, color = get_bmi_category_and_color(bmi)
        st.success(f"Your BMI is **{bmi}**")
        st.markdown(f"<h4>Your BMI Category: <span style='color:{color}'>{category}</span></h4>", unsafe_allow_html=True)

        # Store BMI with timestamp
        user_data = st.session_state.bmi_data.get(user_id, [])
        user_data.append({"date": datetime.datetime.now(), "bmi": bmi})
        st.session_state.bmi_data[user_id] = user_data

# ---------- BMI History Page ----------
elif page == "BMI History & Graph":
    st.title("BMI History & Trend")
    user_id = st.session_state.user_id

    if user_id not in st.session_state.bmi_data or not st.session_state.bmi_data[user_id]:
        st.warning("No BMI data found for this user.")
    else:
        user_data = pd.DataFrame(st.session_state.bmi_data[user_id])
        user_data['date'] = pd.to_datetime(user_data['date'])

        st.dataframe(user_data.sort_values("date", ascending=False), use_container_width=True)

        # Plotting
        fig, ax = plt.subplots()
        ax.plot(user_data["date"], user_data["bmi"], marker="o", linestyle="-", color="teal")
        ax.set_title(f"{user_id}'s BMI Trend")
        ax.set_xlabel("Date")
        ax.set_ylabel("BMI")
        st.pyplot(fig)

        # Export to CSV
        csv = user_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download BMI History as CSV",
            data=csv,
            file_name=f"{user_id}_bmi_history.csv",
            mime='text/csv'
        )

    if st.button("Reset All History"):
        st.session_state.bmi_data[user_id] = []
        st.success("BMI history reset!")

# ---------- Chatbot Page ----------
elif page == "Chatbot (Local)":
    st.title("Smart Health Chatbot (Local)")
    prompt = st.text_input("Ask me anything about your BMI or health:")
    user_id = st.session_state.user_id

    def generate_response(prompt):
        last_bmi = None
        if user_id in st.session_state.bmi_data and st.session_state.bmi_data[user_id]:
            last_bmi = st.session_state.bmi_data[user_id][-1]['bmi']

        if "bmi" in prompt.lower() and last_bmi:
            cat, _ = get_bmi_category_and_color(last_bmi)
            return f"Your last recorded BMI is {last_bmi} which falls under **{cat}** category."
        elif "how to improve" in prompt.lower() or "tips" in prompt.lower():
            return "Maintain a balanced diet, exercise regularly, and track progress weekly. Would you like a sample routine?"
        elif "normal bmi" in prompt.lower():
            return "A normal BMI range is typically between 18.5 and 24.9."
        else:
            return "I'm here to help with your BMI and health tips. Try asking: 'What was my last BMI?' or 'How to reduce BMI?'"

    if prompt:
        response = generate_response(prompt)
        st.markdown(f"**Chatbot:** {response}")