import streamlit as st
import joblib
import numpy as np
import pandas as pd
# from sklearn.preprocessing import StandardScaler
import pickle
from datetime import datetime

# Load the model
# cat_model = pickle.load('C:/Users/kgarg/PycharmProjects/Zummit_House_Price_Predic/catboost_model.pkl')


with open('C:/Users/kgarg/PycharmProjects/Zummit_House_Price_Predic/catboost_model.pkl', 'rb') as file:
    cat_model = pickle.load(file)

with open('C:/Users/kgarg/PycharmProjects/Zummit_House_Price_Predic/Scaler1.pkl', 'rb') as file:
    scaler = joblib.load(file)

# Function to make predictions
# def make_prediction(input_data):
#     # Convert input data to DataFrame
#     input_df = pd.DataFrame([input_data])
#
#     # Apply the loaded scaler to the input data
#     input_scaled = scaler.transform(input_df)
#
#     # Make prediction
#     prediction = cat_model.predict(input_scaled)
#     return prediction


# # Streamlit app layout
# st.title("House Price Prediction")
#
# st.write("""
# ## Input the following details:
# """)
#
# # Display ranges and collect user input
# st.write("### Latitude")
# lat = st.number_input('Latitude', min_value=47.1559, max_value=47.7776, value=47.5)
# st.write("Min: 47.1559, Max: 47.7776")
#
# st.write("### Longitude")
# long_converted = st.number_input('Longitude', min_value=-122.519, max_value=-121.315, value=-122.0)
# st.write("Min: -122.519, Max: -121.315")
#
# st.write("### Living Measure")
# st.write("Enter the square footage of the interior living space of the home. This includes areas like bedrooms, bathrooms, and living rooms.")
# living_measure = st.number_input('Living Measure (Square Footage)', min_value=290.0, max_value=13540.0, value=2000.0)
#
# st.write("### Lot Measure")
# st.write("Enter the square footage of the entire lot or property. This includes the land area around the home, such as the yard and driveway.")
# lot_measure15 = st.number_input('Lot Measure (Square Footage)', min_value=651.0, max_value=871200.0, value=5000.0)
#
# st.write("### Ceiling Measure")
# st.write("Enter the square footage of the house excluding the basement area. This typically includes all floors above ground level.")
# ceil_measure = st.number_input('Ceiling Measure (Square Footage)', min_value=290.0, max_value=9410.0, value=1000.0)
#
# st.write("### Quality")
# quality = st.number_input('Quality', min_value=1.0, max_value=13.0, value=7.0)
# st.write("Min: 1.0, Max: 13.0")
#
# st.write("### Furnished")
# furnished = st.number_input('0 (Not furnished) | 1 (Furnished)', min_value=0, max_value=1, value=0)
# # furnished = st.sidebar.selectbox("Is the house furnished?", ('Yes', 'No'), help="Presence of Furnishings or Amenities")
# # if furnished == 'Yes':
# #     furnished = 1
# # else:
# #     furnished = 0
# # st.write("Min: 0, Max: 1")
#
# st.write("### Year Built")
# yr_built_converted = st.number_input('Year Built', min_value=1900.0, max_value=2015.0, value=1990.0)
# st.write("Min: 1900.0, Max: 2015.0")
#
# st.write("### Coast - House which has a view to a waterfront")
# coast_converted = st.number_input('0 (No) | 1 (Yes)', min_value=0, max_value=1, value=0)
# st.write("Min: 0, Max: 1")
#
# st.write("### Sight")
# st.write("Indicate whether the property has been viewed or has a view. Use a value between 0 (no view) to 4 (excellent view).")
# sight = st.number_input('Sight (0 to 4)', min_value=0.0, max_value=4.0, value=0.0)
# st.write("Min: 0.0, Max: 4.0")
#
# st.write("### Zipcode")
# zipcode = st.number_input('Zipcode', min_value=98001, max_value=98199, value=98101)
# st.write("Min: 98001, Max: 98199")


# def main():
#     # Title
#     st.title("🏠 House Price Predictor")
#
#     # Subtitle
#     st.write("Enter the details of the house to predict its price.")
#
#     # Input fields for user to input data
#     lat = st.sidebar.number_input("Enter the latitude coordinate:", min_value=47.1559, max_value=47.7776, value=47.5,
#                                   help="Latitude Coordinate of the House")
#
#     long_converted = st.sidebar.number_input("Enter the longitude coordinate:", min_value=-122.519, max_value=-121.315,
#                                              value=-122.0, help="Longitude Coordinate of the House")
#
#     zipcode = st.sidebar.number_input("Enter the house zipcode:", min_value=98001, max_value=98199, value=98006,
#                                       help="Zipcode of the House Location")
#
#     living_measure = st.sidebar.number_input("Enter square footage of the house:", min_value=290.0, max_value=13540.0,
#                                              value=5000.0, help="Square Footage of the House")
#
#     ceil_measure = st.sidebar.number_input("Enter square footage of the house excluding basement:", min_value=290.0,
#                                            max_value=9410.0, value=5000.0, help="Square Footage Excluding the Basement")
#
#     lot_measure15 = st.sidebar.number_input("What is the lot size area?", min_value=651.0, max_value=871200.0,
#                                             value=200000.0, help="Lot Size Area as of 2015")
#
#     quality = st.sidebar.number_input("What is the quality of the house?", min_value=1.0, max_value=13.0, value=9.0,
#                                       help="Grade of the House, from the Grading System")
#
#     # getting current year
#     current_year = datetime.now().year
#     yr_built_converted = st.sidebar.number_input("Enter the year the house was built:", min_value=1900.0,
#                                                  max_value=2015.0, value=2010.0, help="Year of House Construction")
#
#     if yr_built_converted > current_year:
#         st.warning(f"Year built cannot be in the future. Please enter a value less than or equal to {current_year}.")
#         st.stop()
#
#     furnished = st.sidebar.selectbox("Is the house furnished?", ('Yes', 'No'),
#                                      help="Presence of Furnishings or Amenities")
#     if furnished == 'Yes':
#         furnished = 1
#     else:
#         furnished = 0
#
#     coast_converted = st.sidebar.selectbox("Does the house have a waterfront?", ('Yes', 'No'),
#                                            help="Presence of a Waterfront")
#     if coast_converted == 'Yes':
#         coast_converted = 1
#     else:
#         coast_converted = 0
#
#     sight = st.sidebar.number_input("Enter value for sight:", min_value=0.0, max_value=4.0, value=2.0,
#                                     help="Number of Times the House Has Been Viewed")
#
#     # Predict button
#     if st.button("Predict Price"):
#         try:
#             # Create a DataFrame with user input
#             input_data = pd.DataFrame([[lat, living_measure, long_converted, quality, furnished, lot_measure15,
#                                         ceil_measure, yr_built_converted, coast_converted, sight, zipcode]],
#                                       columns=['lat', 'living_measure', 'long_converted', 'quality', 'furnished',
#                                                'lot_measure15', 'ceil_measure', 'yr_built_converted', 'coast_converted',
#                                                'sight', 'zipcode'])
#
#             # Apply the scaler to the input data
#             input_data_scaled = scaler.transform(input_data)
#
#             # Predict the price
#             prediction = cat_model.predict(input_data_scaled)[0]
#
#             # Display the result
#             st.success(f"The Estimated Price of The House is: ${prediction:,.2f}")
#
#         except Exception as e:
#             st.warning(f"Something went wrong: {e}. Please check your inputs and try again.")
#
#
# if __name__ == "__main__":
#     main()
#
# # Collect inputs in a dictionary
# input_data = {
#     'lat': lat,
#     'long_converted': long_converted,
#     'living_measure': living_measure,
#     'lot_measure15': lot_measure15,
#     'ceil_measure': ceil_measure,
#     'quality': quality,
#     'furnished': furnished,
#     'yr_built_converted': yr_built_converted,
#     'coast_converted': coast_converted,
#     'sight': sight,
#     'zipcode': zipcode
# }
#
# # Predict button
# if st.button('Predict Price'):
#     prediction = make_prediction(input_data)
#     st.write(f"Predicted House Price: ${prediction[0]:,.2f}")


def make_prediction(input_data):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Apply the loaded scaler to the input data
    input_scaled = scaler.transform(input_df)

    # Make prediction
    prediction = cat_model.predict(input_scaled)
    return prediction

def main():
    # Title
    st.title("🏠 House Price Predictor")

    # Subtitle
    st.write("Enter the details of the house to predict its price.")

    # Input fields for user to input data in the specified order
    lat = st.number_input("Enter the latitude coordinate:", min_value=47.1559, max_value=47.7776, value=47.5,
                          help="Latitude Coordinate of the House (Min: 47.1559, Max: 47.7776)")

    living_measure = st.number_input("Enter square footage of the house:", min_value=290.0, max_value=13540.0,
                                     value=5000.0, help="Square Footage of the House (Min: 290.0, Max: 13540.0)")

    long_converted = st.number_input("Enter the longitude coordinate:", min_value=-122.519, max_value=-121.315,
                                     value=-122.0, help="Longitude Coordinate of the House (Min: -122.519, Max: -121.315)")

    quality = st.number_input("What is the quality of the house?", min_value=1.0, max_value=13.0, value=9.0,
                              help="Grade of the House, from the Grading System (Min: 1.0, Max: 13.0)")

    furnished = st.selectbox("Is the house furnished?", ('Yes', 'No'),
                             help="Presence of Furnishings or Amenities")
    furnished = 1 if furnished == 'Yes' else 0

    lot_measure15 = st.number_input("What is the lot size area?", min_value=651.0, max_value=871200.0,
                                    value=200000.0, help="Lot Size Area as of 2015 (Min: 651.0, Max: 871200.0)")

    ceil_measure = st.number_input("Enter square footage of the house excluding basement:", min_value=290.0,
                                   max_value=9410.0, value=5000.0, help="Square Footage Excluding the Basement (Min: 290.0, Max: 9410.0)")

    # Getting current year
    current_year = datetime.now().year
    yr_built_converted = st.number_input("Enter the year the house was built:", min_value=1900.0,
                                         max_value=float(current_year), value=2010.0,
                                         help=f"Year of House Construction (Min: 1900.0, Max: {current_year})")

    coast_converted = st.selectbox("Does the house have a waterfront?", ('Yes', 'No'),
                                   help="Presence of a Waterfront")
    coast_converted = 1 if coast_converted == 'Yes' else 0

    sight = st.number_input("Enter value for sight:", min_value=0.0, max_value=4.0, value=2.0,
                            help="Number of Times the House Has Been Viewed (Min: 0.0, Max: 4.0)")

    zipcode = st.number_input("Enter the house zipcode:", min_value=98001, max_value=98199, value=98006,
                              help="Zipcode of the House Location (Min: 98001, Max: 98199)")

    # Predict button
    if st.button("Predict Price"):
        try:
            # Collect inputs in a dictionary
            input_data = {
                'lat': lat,
                'living_measure': living_measure,
                'long_converted': long_converted,
                'quality': quality,
                'furnished': furnished,
                'lot_measure15': lot_measure15,
                'ceil_measure': ceil_measure,
                'yr_built_converted': yr_built_converted,
                'coast_converted': coast_converted,
                'sight': sight,
                'zipcode': zipcode
            }

            # Make prediction
            prediction = make_prediction(input_data)

            # Display the result
            st.success(f"The Estimated Price of The House is: ${prediction[0]:,.2f}")

        except Exception as e:
            st.warning(f"Something went wrong: {e}. Please check your inputs and try again.")

if __name__ == "__main__":
    main()