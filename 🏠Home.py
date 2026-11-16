# import streamlit as st

# st.title("Solar Power Generation Prediction")
# st.write("Welcome to the Solar Power Generation Prediction tool.")
# st.write("This tool helps you predict the solar energy output based on weather conditions.")
# st.write("Use the 'User Enter Data' tab to input the weather details for your location.")
# st.write("use the GPS tracking for access")
# # Add a title for the section
# st.title("Benefits of Solar Power for Household Usage")
# # Write the content using st.write or st.markdown
# st.markdown("""
#     1. Significant Savings on Electricity Bills:
#     Reduced Monthly Expenses: Solar power systems generate electricity during daylight hours, reducing reliance on grid power. This directly translates to lower electricity bills.
#     Long-Term Savings: While the initial investment in a solar power system can be significant, the long-term savings over the system's lifespan can be substantial.
#     Example:
#     Let's assume a family's monthly electricity bill is ₹2,400. By installing a solar power system, they can generate a significant portion of their electricity needs, reducing their
#         monthly bill to, say, ₹1,000. Over a year, this translates to a saving of
#     Annual Saving: ₹(2,400 - 1,000) * 12 = ₹16,800
#     2. Government Incentives and Subsidies:
#     Subsidies: The Indian government offers various subsidies and incentives to promote solar power adoption. These subsidies can significantly reduce the upfront cost of installing a solar power system.
#     Tax Benefits: Solar power systems can also qualify for certain tax benefits, further reducing the overall cost.
#     3. Environmental Benefits and Sustainable Living:
#     Reduced Carbon Footprint: Solar energy is a clean and renewable source of energy. By using solar power, you contribute to reducing greenhouse gas emissions and combating climate change.
#     Energy Independence: Solar power systems can help reduce reliance on traditional, fossil fuel-based power sources, making you more energy independent.
#     4. Potential for Additional Income:
#     Net Metering: Many states in India have net metering policies, allowing you to sell excess solar power generated to the grid. This can provide additional income.""")
#     # User Enter Data Tab 🏠Home.py
import streamlit as st

st.set_page_config(
    page_title="Solar Power Generation Prediction",
    page_icon="☀️",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    .hero {
        background: linear-gradient(135deg, #BDC4D4 0%, #52677D 100%);
        padding: 3rem 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 2.6rem;
        margin-bottom: 0.5rem;
    }
    .hero p {
        font-size: 1.15rem;
        opacity: 0.95;
        max-width: 750px;
    }
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    .benefit-card {
        background: #52677D;
        border: 1px solid #eee;
        border-left: 5px solid #BDC4D4;
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        height: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 1rem;
    }
    .benefit-card h4 {
        margin-top: 0;
        color: #1c2e4a;
    }
    .stat-box {
        background: #52677D;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
    }
    .stat-box h2 {
        color: #BDC4D4;
        margin-bottom: 0;
    }
    .cta {
        background: #1a1a1a;
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-top: 2rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
    <div class="hero">
        <h1>☀️ Solar Power Generation Prediction</h1>
        <p>
            Estimate solar energy output for any location using live weather data and
            machine learning — helping you make informed decisions about solar plant
            suitability before you invest.
        </p>
    </div>
""", unsafe_allow_html=True)

# ---------- QUICK STATS ----------
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class="stat-box">
            <h2>3-Day</h2>
            <p>Weather-based forecast</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="stat-box">
            <h2>GPS</h2>
            <p>Location-aware predictions</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class="stat-box">
            <h2>ML</h2>
            <p>Trained prediction model</p>
        </div>
    """, unsafe_allow_html=True)

# ---------- HOW TO USE ----------
st.markdown('<div class="section-title">🚀 How to Use This Tool</div>', unsafe_allow_html=True)
st.markdown("""
- Open the **User Enter Data** tab to input weather details manually for your location, or
- Enable **GPS tracking** to automatically detect your location and fetch live weather data.
- View your predicted solar output along with a suitability verdict (Suitable, Marginal, or Unsuitable).
""")

# ---------- BENEFITS SECTION ----------
st.markdown('<div class="section-title">🌟 Benefits of Solar Power for Household Usage</div>', unsafe_allow_html=True)

b1, b2 = st.columns(2)

with b1:
    st.markdown("""
        <div class="benefit-card">
            <h4>💰 Significant Savings on Electricity Bills</h4>
            Solar systems generate electricity during daylight hours, reducing reliance on grid power
            and lowering monthly bills. For example, a family paying ₹2,400/month could reduce their
            bill to around ₹1,000 — saving roughly <b>₹16,800 per year</b>.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="benefit-card">
            <h4>🏛️ Government Incentives &amp; Subsidies</h4>
            The Indian government offers subsidies and tax benefits to promote solar adoption,
            significantly reducing the upfront cost of installation.
        </div>
    """, unsafe_allow_html=True)

with b2:
    st.markdown("""
        <div class="benefit-card">
            <h4>🌍 Environmental Benefits</h4>
            Solar energy is clean and renewable. Using it reduces your carbon footprint and
            reliance on fossil fuels, supporting a more sustainable way of living.<br><br> 
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="benefit-card">
            <h4>📈 Potential for Additional Income</h4>
            With net metering policies available in many Indian states, you can sell excess
            solar power back to the grid — turning your rooftop into a source of income.
        </div>
    """, unsafe_allow_html=True)

# ---------- CALL TO ACTION ----------
st.markdown("""
    <div class="cta">
        <h3>Ready to check your solar potential?</h3>
        <p>Head to the <b>User Enter Data</b> tab and get your personalized prediction in seconds.</p>
    </div>
""", unsafe_allow_html=True)