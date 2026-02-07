import streamlit as st
def convert_length(value, from_unit, to_unit):
    # Define conversion factors to meters
    conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    }
    
    # Convert the input value to meters
    value_in_meters = value * conversion_factors[from_unit]
    
    # Convert from meters to the target unit
    converted_value = value_in_meters / conversion_factors[to_unit]
    
    return converted_value

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return None

def convert_weight(value, from_unit, to_unit):
    # Define conversion factors to grams
    conversion_factors = {
        'grams': 1,
        'kilograms': 1000,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    
    # Convert the input value to grams
    value_in_grams = value * conversion_factors[from_unit]
    
    # Convert from grams to the target unit
    converted_value = value_in_grams / conversion_factors[to_unit]
    
    return converted_value

def main():
    st.title("Unit Converter")
    
    conversion_type = st.selectbox("Select conversion type", ["Length", "Temperature", "Weight"])
    
    if conversion_type == "Length":
        from_unit = st.selectbox("From", ["meters", "kilometers", "miles", "feet", "inches"])
        to_unit = st.selectbox("To", ["meters", "kilometers", "miles", "feet", "inches"])
        value = st.number_input("Value to convert")
        if st.button("Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
    
    elif conversion_type == "Temperature":
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        value = st.number_input("Value to convert")
        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
    
    elif conversion_type == "Weight":
        from_unit = st.selectbox("From", ["grams", "kilograms", "pounds", "ounces"])
        to_unit = st.selectbox("To", ["grams", "kilograms", "pounds", "ounces"])
        value = st.number_input("Value to convert")
        if st.button("Convert"):
            result = convert_weight(value, from_unit, to_unit)
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

if __name__ == "__main__":
    main()


