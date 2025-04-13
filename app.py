# import streamlit as st
# import pickle
# import pandas as pd

# # Define Teams and Cities
# teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
#          'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
#          'Rajasthan Royals', 'Delhi Capitals','Gujarat Titans', 'Lucknow Super Giants']

# cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
#           'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
#           'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
#           'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
#           'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
#           'Sharjah', 'Mohali', 'Bengaluru']

# # Load the model
# pipe = pickle.load(open('pipe.pkl', 'rb'))

# # Customizing Page Layout
# st.set_page_config(page_title='IPL Match Win Predictor', page_icon='🏏', layout='centered')

# # Apply Custom Styling
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #121212;
#         color: white;
#     }
#     .stButton>button {
#         background-color: #fdd835;
#         color: black;
#         font-weight: bold;
#         border-radius: 8px;
#         padding: 10px 20px;
#     }
#     .stButton>button:hover {
#         background-color: #ffeb3b;
#         transform: scale(1.05);
#     }
#     </style>
# """, unsafe_allow_html=True)

# # App Title with Styling
# st.markdown("""
#     <h1 style='text-align: center; color: #FFD700;'>🏆 IPL Match Win Predictor</h1>
#     <p style='text-align: center; font-size: 18px;'>Predict the winning probability of teams in an IPL match</p>
# """, unsafe_allow_html=True)

# # Input Columns
# col1, col2 = st.columns(2)

# with col1:
#     batting_team = st.selectbox('Batting Team', sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Bowling Team', sorted(teams))

# selected_city = st.selectbox('Host City', sorted(cities))

# target = st.number_input('Target Score', min_value=1, step=1)

# # Match Stats Input
# col3, col4, col5 = st.columns(3)

# with col3:
#     score = st.number_input('Current Score', min_value=0, step=1)

# with col4:
#     overs_int = st.number_input('Overs Completed', min_value=0, max_value=20, step=1)
#     balls = st.number_input('Balls in Current Over', min_value=0, max_value=6, step=1)
#     overs = overs_int + (balls / 6.0)
# with col5:
#     wickets_out = st.number_input('Wickets Lost', min_value=0, max_value=10, step=1)

# # Prediction Button with Styling
# if st.button('Predict Probability'):
#     runs_left = target - score
#     balls_left = 120 - (overs * 6)
#     wickets_remaining = 10 - wickets_out

#     crr = score / overs if overs > 0 else 0
#     rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

#     input_df = pd.DataFrame({
#         'batting_team': [batting_team],
#         'bowling_team': [bowling_team],
#         'city': [selected_city],
#         'runs_left': [runs_left],
#         'balls_left': [balls_left],
#         'wickets': [wickets_remaining],
#         'total_runs_x': [target],
#         'crr': [crr],
#         'rrr': [rrr]
#     })

#     result = pipe.predict_proba(input_df)
#     loss = result[0][0]
#     win = result[0][1]

#     st.markdown(f"""
#         <div style='text-align: center;'>
#             <h2 style='color: #32CD32;'>🏏 {batting_team} Win Probability: {round(win * 100)}%</h2>
#             <h2 style='color: #FF4500;'>🏏 {bowling_team} Win Probability: {round(loss * 100)}%</h2>
#         </div>
#     """, unsafe_allow_html=True)





# //2ND PARA OF CODE


# import streamlit as st
# import pickle
# import pandas as pd
# import base64
# import os

# # --- Image Loading Function ---
# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode('utf-8')

# # Verify image exists
# image_path = 'stadium background 2.jpg'
# if not os.path.exists(image_path):
#     st.error(f"Error: Image not found at {os.path.abspath(image_path)}")
# else:
#     bg_image = get_base64_image(image_path)

# # --- Model Data ---
# teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
#          'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
#          'Rajasthan Royals', 'Delhi Capitals']

# # 'Gujarat Titans', 'Lucknow Super Giants'

# cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
#           'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
#           'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
#           'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
#           'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
#           'Sharjah', 'Mohali', 'Bengaluru']

# pipe = pickle.load(open('pipe.pkl', 'rb'))

# # --- Page Config ---
# st.set_page_config(
#     page_title='IPL Match Win Predictor', 
#     page_icon='🏏', 
#     layout='centered'
# )

# # --- CSS with Enhanced Visibility ---
# st.markdown(f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/jpg;base64,{bg_image}");
#         background-size: cover;
#         background-position: center;
#         background-attachment: fixed;
#     }}
#     /* Darker overlay for better contrast */
#     .stApp::before {{
#         content: "";
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         bottom: 0;
#         background: rgba(0, 0, 0, 0.75);
#         z-index: 0;
#     }}
#     /* Main content container */
#     .main .block-container {{
#         background-color: rgba(0, 0, 0, 0.85);
#         border-radius: 10px;
#         padding: 2rem;
#         border: 1px solid #444;
#         box-shadow: 0 4px 20px rgba(0,0,0,0.5);
#     }}
#     /* Text elements */
#     .stMarkdown, .stSelectbox label, .stNumberInput label {{
#         color: white !important;
#         text-shadow: 1px 1px 2px black;
#     }}
#     /* Input fields */
#     .stSelectbox, .stNumberInput {{
#         background-color: rgba(255,255,255,0.15) !important;
#         border-radius: 8px;
#         padding: 8px;
#     }}
#     /* Button styling */
#     .stButton>button {{
#         background-color: #fdd835;
#         color: black !important;
#         font-weight: bold;
#         border-radius: 8px;
#         padding: 10px 20px;
#         font-size: 1rem;
#         margin: 0 auto;
#         display: block;
#         width: 200px;
#     }}
#     .stButton>button:hover {{
#         background-color: #ffeb3b;
#         transform: scale(1.05);
#     }}
#     /* Prediction result box */
#     .prediction-box {{
#         background-color: rgba(0, 0, 0, 0.85) !important;
#         border: 1px solid #444;
#         border-radius: 10px;
#         padding: 20px;
#         margin-top: 20px;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.4);
#     }}
#     </style>
# """, unsafe_allow_html=True)

# # --- App Title ---
# st.markdown("""
#     <div style='text-align: center;'>
#         <h1 style='color: #FFD700; text-shadow: 2px 2px 4px #000000; margin-bottom: 0.5rem;'>
#             🏆 IPL Match Win Predictor
#         </h1>
#         <p style='color: white; font-size: 1.1rem; text-shadow: 1px 1px 2px black;'>
#             Predict the winning probability of teams in an IPL match
#         </p>
#     </div>
# """, unsafe_allow_html=True)

# # --- Input Section ---
# col1, col2 = st.columns(2)
# with col1:
#     batting_team = st.selectbox('Batting Team', sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Bowling Team', sorted(teams))

# selected_city = st.selectbox('Host City', sorted(cities))
# target = st.number_input('Target Score', min_value=1, step=1)

# col3, col4, col5 = st.columns(3)
# with col3:
#     score = st.number_input('Current Score', min_value=0, step=1)
# with col4:
#     overs_int = st.number_input('Overs Completed', min_value=0, max_value=20, step=1)
#     balls = st.number_input('Balls in Current Over', min_value=0, max_value=6, step=1)
#     overs = overs_int + (balls / 6.0)
# with col5:
#     wickets_out = st.number_input('Wickets Lost', min_value=0, max_value=10, step=1)

# # --- Prediction Logic ---
# if st.button('Predict Probability'):
#     runs_left = target - score
#     balls_left = 120 - (overs * 6)
#     wickets_remaining = 10 - wickets_out

#     crr = score / overs if overs > 0 else 0
#     rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

#     input_df = pd.DataFrame({
#         'batting_team': [batting_team],
#         'bowling_team': [bowling_team],
#         'city': [selected_city],
#         'runs_left': [runs_left],
#         'balls_left': [balls_left],
#         'wickets': [wickets_remaining],
#         'total_runs_x': [target],
#         'crr': [crr],
#         'rrr': [rrr]
#     })

#     result = pipe.predict_proba(input_df)
#     loss = result[0][0]
#     win = result[0][1]

#     st.markdown(f"""
#         <div class='prediction-box'>
#             <h2 style='color: #32CD32; text-align: center; text-shadow: 1px 1px 2px black;'>
#                 🏏 {batting_team} Win Probability: {round(win * 100)}%
#             </h2>
#             <h2 style='color: #FF4500; text-align: center; text-shadow: 1px 1px 2px black;'>
#                 🏏 {bowling_team} Win Probability: {round(loss * 100)}%
#             </h2>
#         </div>
#     """, unsafe_allow_html=True)








# //3RD PARA OF CODE



import streamlit as st
import pickle
import pandas as pd
import base64
import os

# --- Image Loading Function ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

image_path = 'stadium background 2.jpg'
if not os.path.exists(image_path):
    st.error(f"Error: Image not found at {os.path.abspath(image_path)}")
else:
    bg_image = get_base64_image(image_path)

# --- Model Data ---
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl', 'rb'))

# --- Page Config ---
st.set_page_config(
    page_title='IPL Match Win Predictor',
    page_icon='🏏',
    layout='centered'
)

# --- CSS Styling ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.75);
        z-index: 0;
    }}
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.85);
        border-radius: 10px;
        padding: 2rem;
        border: 1px solid #444;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }}
    .stMarkdown, .stSelectbox label, .stNumberInput label {{
        color: white !important;
        text-shadow: 1px 1px 2px black;
    }}
    .stSelectbox, .stNumberInput {{
        background-color: rgba(255,255,255,0.15) !important;
        border-radius: 8px;
        padding: 8px;
    }}
    .stButton>button {{
        background-color: #fdd835;
        color: black !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 1rem;
        margin: 0 auto;
        display: block;
        width: 200px;
    }}
    .stButton>button:hover {{
        background-color: #ffeb3b;
        transform: scale(1.05);
    }}
    .prediction-box {{
        background-color: rgba(0, 0, 0, 0.85) !important;
        border: 1px solid #444;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }}
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #FFD700; text-shadow: 2px 2px 4px #000000; margin-bottom: 0.5rem;'>
            🏆 IPL Match Win Predictor
        </h1>
        <p style='color: white; font-size: 1.1rem; text-shadow: 1px 1px 2px black;'>
            Predict the winning probability of teams in an IPL match
        </p>
    </div>
""", unsafe_allow_html=True)

# --- Input UI ---
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Batting Team', sorted(teams), key='batting')
with col2:
    bowling_team = st.selectbox('Bowling Team', sorted(teams), key='bowling')

selected_city = st.selectbox('Host City', sorted(cities), key='city')
target = st.number_input('Target Score', min_value=1, step=1, key='target')

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Current Score', min_value=0, step=1, key='score')
with col4:
    overs_int = st.number_input('Overs Completed', min_value=0, max_value=20, step=1, key='overs_int')
    balls = st.number_input('Balls in Current Over', min_value=0, max_value=6, step=1, key='balls')
    overs = overs_int + (balls / 6.0)
with col5:
    wickets_out = st.number_input('Wickets Lost', min_value=0, max_value=10, step=1, key='wickets')

# --- Determine Match Status ---
match_over = False
match_result = ""

if score >= target:
    match_over = True
    match_result = f"""
        <div class='prediction-box'>
            <h2 style='color: #32CD32; text-align: center; text-shadow: 1px 1px 2px black;'>
                🏏 {batting_team} has already won the match! 🎉
            </h2>
        </div>
    """
elif overs >= 20 and score < target:
    match_over = True
    match_result = f"""
        <div class='prediction-box'>
            <h2 style='color: #FF4500; text-align: center; text-shadow: 1px 1px 2px black;'>
                🏏 {bowling_team} has won the match! 🏆
            </h2>
        </div>
    """

# --- Team Validation ---
team_error = False
if batting_team == bowling_team:
    st.error("⚠️ Batting and Bowling teams cannot be the same.")
    team_error = True

# --- Button ---
predict_btn = st.button('Predict Probability', disabled=(match_over or team_error))

# --- Prediction ---
if predict_btn:
    if not match_over and not team_error:
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
            <div class='prediction-box'>
                <h2 style='color: #32CD32; text-align: center; text-shadow: 1px 1px 2px black;'>
                    🏏 {batting_team} Win Probability: {round(win * 100)}%
                </h2>
                <h2 style='color: #FF4500; text-align: center; text-shadow: 1px 1px 2px black;'>
                    🏏 {bowling_team} Win Probability: {round(loss * 100)}%
                </h2>
            </div>
        """, unsafe_allow_html=True)

# --- Final Result if Match Over ---
if match_result:
    st.markdown(match_result, unsafe_allow_html=True)

