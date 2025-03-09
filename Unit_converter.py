import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversions = {
        "Meters": 1,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Kilometers": 0.001,
        "Miles": 0.000621371
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value  # No conversion needed if same unit

def main():
    st.title("Unit Converter App")

    category = st.selectbox("Select conversion category", ["Length", "Temperature"])

    if category == "Length":
        value = st.number_input("Enter value", min_value=0.0, format="%.2f")
        from_unit = st.selectbox("From", ["Meters", "Feet", "Inches", "Kilometers", "Miles"])
        to_unit = st.selectbox("To", ["Meters", "Feet", "Inches", "Kilometers", "Miles"])
        if st.button("Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

    elif category == "Temperature":
        value = st.number_input("Enter value", format="%.2f")
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()
