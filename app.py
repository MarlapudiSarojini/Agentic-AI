import streamlit as st
from weather_agent import get_weather
from content_agent import generate_weather_report
from pdf_agent import create_pdf

st.title("🌦️ Multi-Agent Weather Report System")

city = st.text_input("Enter City Name")

if st.button("Generate Weather Report"):
    if city:
        weather_data = get_weather(city)
        report = generate_weather_report(weather_data)
        pdf_file = create_pdf(report)

        st.subheader("📄 Weather Summary")
        st.write(report)

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📥 Download PDF Report",
                data=file,
                file_name="weather_report.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Please enter a city name")
