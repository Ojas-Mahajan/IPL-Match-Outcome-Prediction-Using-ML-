import streamlit as st
import pickle
import pandas as pd
#  2 new lines added
import sklearn
print("SKLEARN VERSION:", sklearn.__version__)


# Define Teams and Cities
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals',]

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# Load the model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Customizing Page Layout
st.set_page_config(page_title='IPL Match Win Predictor', page_icon='🏏', layout='centered')

# Apply Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: white;
    }
    .stButton>button {
        background-color: #fdd835;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ffeb3b;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# App Title with Styling
st.markdown("""
    <h1 style='text-align: center; color: #FFD700;'>🏆 IPL Match Win Predictor</h1>
    <p style='text-align: center; font-size: 18px;'>Predict the winning probability of teams in an IPL match</p>
""", unsafe_allow_html=True)

# Input Columns
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Bowling Team', sorted(teams))

selected_city = st.selectbox('Host City', sorted(cities))

target = st.number_input('Target Score', min_value=1, step=1)

# Match Stats Input
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score', min_value=0, step=1)

with col4:
    overs_int = st.number_input('Overs Completed', min_value=0, max_value=20, step=1)
    balls = st.number_input('Balls in Current Over', min_value=0, max_value=6, step=1)
    overs = overs_int + (balls / 6.0)
with col5:
    wickets_out = st.number_input('Wickets Lost', min_value=0, max_value=10, step=1)

# Prediction Button with Styling
if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_remaining = 10 - wickets_out

    crr = score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_remaining],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    st.markdown(f"""
        <div style='text-align: center;'>
            <h2 style='color: #32CD32;'>🏏 {batting_team} Win Probability: {round(win * 100)}%</h2>
            <h2 style='color: #FF4500;'>🏏 {bowling_team} Win Probability: {round(loss * 100)}%</h2>
        </div>
    """, unsafe_allow_html=True)



