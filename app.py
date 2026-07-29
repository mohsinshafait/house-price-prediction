# Basic Structure

import streamlit as st

import streamlit as st

from utils import (
    load_model,
    load_default_values,
    load_dropdown_options,
    create_input_dataframe,
    predict_price
)

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load Model

@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# Load Defualt Values

defaults = load_default_values()

# Load Dropdown Options

dropdown_options = load_dropdown_options()

# Side Bar

with st.sidebar:

    st.title("🏠 House Price Prediction")

    st.markdown("---")

    st.subheader("📊 Model")

    st.write("Gradient Boosting Regressor")

    st.subheader("🗃️ Data")

    st.write("Ames Housing Dataset")

    st.subheader("📈 Performance")

    st.write("R² Score: 0.912")
    st.write("RMSE: $26,552")
    st.write("MAE: $15,435")

    st.markdown("---")



# Title

st.title("🏠 House Price Prediction")

st.caption(
    "Estimate residential property prices using Machine Learning."
)
# Description

st.markdown("""

Enter the property details below and click **Predict House Price**.
""")

# Horizontal devider
st.divider()

#  Form

with st.form("prediction_form"):

    # General Information
    # st.subheader("📋 General Information")
    with st.expander("📋 General Information", expanded=True):

        overall_qual = st.slider(
            "Overall Quality",
            min_value=1,
            max_value=10,
            value=int(defaults["Overall Qual"]),
            help="Overall material and finish quality."
        )

        overall_cond = st.slider(
            "Overall Condition",
            min_value=1,
            max_value=10,
            value=int(defaults["Overall Cond"]),
            help="Overall condition of the house."
        )

    # Property Size

    # st.subheader("📐 Property Size")
    with st.expander("📐 Property Size", expanded=False):
        living_area = st.number_input(
            "Above Ground Living Area (sq ft)",
            min_value=300,
            value=int(defaults["Gr Liv Area"])
        )

        lot_area = st.number_input(
            "Lot Area (sq ft)",
            min_value=1000,
            value=int(defaults["Lot Area"])
        )

        basement_area = st.number_input(
            "Total Basement Area (sq ft)",
            min_value=0,
            value=int(defaults["Total Bsmt SF"])
        )

    # Construction

    # st.subheader("🏗 Construction")
    with st.expander("🏗 Construction", expanded=False):
        year_built = st.number_input(
            "Year Built",
            min_value=1872,
            max_value=2026,
            value=int(defaults["Year Built"])
        )

        year_remod = st.number_input(
            "Year Remodeled",
            min_value=1950,
            max_value=2026,
            value=int(defaults["Year Remod/Add"])
        )

    # Garage and Rooms

    # st.subheader("🚗 Garage & Rooms")
    with st.expander("🚗 Garage & Rooms", expanded=False):
        
        garage_cars = st.number_input(
            "Garage Capacity (Cars)",
            min_value=0,
            max_value=5,
            value=int(defaults["Garage Cars"])
        )

        full_bath = st.number_input(
            "Full Bathrooms",
            min_value=0,
            max_value=5,
            value=int(defaults["Full Bath"])
        )

        fireplaces = st.number_input(
            "Number of Fireplaces",
            min_value=0,
            max_value=4,
            value=int(defaults["Fireplaces"])
        )

    # Drop Down Option
    with st.expander("⭐ Property Quality", expanded=False):
    # st.subheader("⭐ Property Quality")

        kitchen_quality = st.selectbox(
            "Kitchen Quality",
            dropdown_options["Kitchen Qual"],
            index=dropdown_options["Kitchen Qual"].index(defaults["Kitchen Qual"])
        )

        basement_quality = st.selectbox(
            "Basement Quality",
            dropdown_options["Bsmt Qual"],
            index=dropdown_options["Bsmt Qual"].index(defaults["Bsmt Qual"])
        )

        neighborhood = st.selectbox(
            "Neighborhood",
            dropdown_options["Neighborhood"],
            index=dropdown_options["Neighborhood"].index(defaults["Neighborhood"])
        )


    predict_button = st.form_submit_button(
    "💰 Predict House Price",
    use_container_width=True
)

    # Uer Dictionary

    if predict_button:

        user_inputs = {
            "Overall Qual": overall_qual,
            "Overall Cond": overall_cond,
            "Gr Liv Area": living_area,
            "Lot Area": lot_area,
            "Total Bsmt SF": basement_area,
            "Garage Cars": garage_cars,
            "Full Bath": full_bath,
            "Fireplaces": fireplaces,
            "Year Built": year_built,
            "Year Remod/Add": year_remod,
            "Kitchen Qual": kitchen_quality,
            "Bsmt Qual": basement_quality,
            "Neighborhood": neighborhood
        }

        with st.spinner("Predicting house price..."):

            input_df = create_input_dataframe(user_inputs)

            prediction = predict_price(model, input_df)

            st.success("Prediction generated successfully!")

            st.divider()

            st.subheader("💰 Estimated House Price")

            st.metric(
                label="Predicted Selling Price",
                value=f"${prediction:,.0f}"
            )
            st.info(
    """
    This prediction is generated by a machine learning model and
    should be considered an estimate rather than an exact market value.
    """
)

st.divider()

st.caption(
    "Developed by Mohsin Shafait • Machine Learning Portfolio Project"
)

# # Columns

# col1, col2 = st.columns(2)

# # Left Column

# with col1:

#     st.subheader("General Information")

#     overall_qual = st.slider(
#         "Overall Quality",
#         1,
#         10,
#         5
#     )

#     overall_cond = st.slider(
#         "Overall Condition",
#         1,
#         10,
#         5
#     )

#     lot_area = st.number_input(
#         "Lot Area (sq ft)",
#         min_value=1000,
#         value=9000
#     )

#     living_area = st.number_input(
#         "Living Area (sq ft)",
#         min_value=300,
#         value=1500
#     )

#     basement_area = st.number_input(
#         "Basement Area (sq ft)",
#         min_value=0,
#         value=1000
#     )


# # Right Column

# with col2:

#     st.subheader("Property Details")

#     garage_cars = st.number_input(
#         "Garage Capacity",
#         min_value=0,
#         max_value=5,
#         value=2
#     )

#     full_bath = st.number_input(
#         "Full Bathrooms",
#         min_value=0,
#         max_value=5,
#         value=2
#     )

#     fireplaces = st.number_input(
#         "Fireplaces",
#         min_value=0,
#         max_value=4,
#         value=1
#     )

#     year_built = st.number_input(
#         "Year Built",
#         min_value=1870,
#         max_value=2026,
#         value=1975
#     )

#     year_remod = st.number_input(
#         "Year Remodeled",
#         min_value=1950,
#         max_value=2026,
#         value=1975
#     )


