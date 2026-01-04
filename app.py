import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="The Sovereign Investor Manual", layout="wide")

st.title("📖 The Ultimate Beginner’s Guide to Financial Markets")
st.subheader("From Understanding to Owning: A 5-Page Action Plan")

# --- SIDEBAR: COMPOUND INTEREST EXPLAINED ---
st.sidebar.header("⏳ The Magic of Compound Interest")
st.sidebar.write("""
Compound interest is when the interest you earn on your money begins to earn interest itself. 
Over time, this creates an 'exponential' curve where your wealth grows faster every year.
""")

principal = st.sidebar.number_input("Starting Investment (Principal)", value=1000, step=100)
rate = st.sidebar.slider("Expected Annual Return (%)", 1, 20, 8)
years = st.sidebar.slider("Number of Years to Hold", 1, 50, 25)

# Calculation
total_value = principal * (1 + (rate/100))**years
profit = total_value - principal

st.sidebar.divider()
st.sidebar.metric("Final Balance", f"{total_value:,.2f}")
st.sidebar.write(f"Your original investment grew by **{profit:,.2f}** due to time and compounding.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. The Building Blocks", 
    "2. Where Trading Happens", 
    "3. Mechanics of the Trade", 
    "4. Deep Water (Advanced)", 
    "5. The Execution Process"
])

with tab1:
    st.header("Page 1: The Definitions (Clearing the Fog)")
    st.write("To act, you must speak the language. Let's fix the basic confusion.")

    st.subheader("🍕 Stock vs. Shares vs. Equities")
    st.write("""
    - **Equities:** This is the broad category of 'ownership.'
    - **Stock:** This is the 'stuff' you own. (e.g., 'I own stock in the tech sector.')
    - **Shares:** These are the units. 
    
    **The Pizza Metaphor:** If a company is a pizza, the **Stock** is the flavor (Pepperoni), and the **Shares** are the individual slices. You buy 10 slices (shares) of the Apple pizza.
    """)
    

    st.subheader("📜 Securities vs. Commodities")
    st.write("""
    - **Securities:** These are 'financial papers' that represent a claim on value. This includes **Stocks** (ownership) and **Bonds** (loans).
    - **Bonds (The I.O.U.):** When you buy a bond, you are a **Lender**. You give money to a government or company, and they promise to pay you back with interest. They are safer because if a company goes broke, bondholders get paid before stockholders.
    - **Commodities:** These are 'Physical Stuff' like Gold, Oil, or Wheat. You only make money here if the price of the raw material goes up.
    """)

    st.subheader("🧺 The 'Basket' (The Best Way to Buy)")
    st.write("""
    You should rarely buy individual shares. Instead, you buy **Funds**.
    - **ETF (Exchange Traded Fund):** A basket that trades like a stock on your phone.
    - **Mutual Fund:** A basket that trades only once a day at 4:00 PM.
    - **Index Fund:** A 'recipe' that tells a Fund to just buy the 500 biggest companies (like the S&P 500) and do nothing else.
    """)

with tab2:
    st.header("Page 2: Where and How Trading Happens")
    st.write("You don't buy stocks from a person on the street; you use a Market Architecture.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏛️ 1. The Exchanges (The Marketplace)")
        st.write("""
        The Exchange is the digital platform where buyers and sellers meet.
        - **NYSE (New York Stock Exchange):** The giant home of massive companies.
        - **NASDAQ:** Where the tech world (Apple, Google) lives.
        - **CBOE:** Where Options and Derivatives are traded.
        - **NGX (Nigerian Exchange):** Where local giants like Dangote and MTN are traded.
        """)

    with col2:
        st.subheader("🚪 2. The Broker (The Gatekeeper)")
        st.write("""
        You cannot walk onto the floor of the NYSE. You must use a **Brokerage** (e.g., Fidelity, Vanguard, Bamboo, or Zenith Assets).
        - **Their Job:** They take your order and execute it on the Exchange for you.
        """)

    st.subheader("💰 3. How Prices are Set")
    st.write("""
    Prices are determined by the **Bid-Ask Spread**:
    - **Bid:** The highest price a buyer is willing to pay.
    - **Ask:** The lowest price a seller is willing to accept.
    - The 'Price' you see on Google is just the last price where a buyer and seller actually agreed to a deal.
    """)
    

with tab3:
    st.header("Page 3: Mechanics of the Trade (Step-by-Step)")
    st.write("When you open your app, you have to choose *how* to buy.")

    st.subheader("🛒 Market Orders vs. Limit Orders")
    st.write("""
    - **Market Order:** 'Buy this for me right now at whatever the current price is.' (Fast, but you might pay more than you expected).
    - **Limit Order:** 'Only buy this if the price hits $150 or lower.' **Always use Limit Orders** so you control your costs.
    """)

    st.subheader("🕒 Trading Hours")
    st.write("""
    - **Standard Hours:** 9:30 AM to 4:00 PM EST. This is when the most people are trading ('Liquidity').
    - **After-Hours:** Trading is possible but risky because fewer people are active, causing prices to jump wildly.
    """)

    st.subheader("🚚 Settlement (T+1)")
    st.write("""
    When you sell a stock, the cash isn't 'yours' to withdraw instantly. It takes **one business day** (T+1) for the electronic paperwork to clear.
    """)

with tab4:
    st.header("Page 4: Advanced Trading (The Deep Water)")
    st.write("This is how professionals move money through contracts.")

    st.subheader("🎲 Derivatives (The Contracts)")
    st.write("""
    You aren't buying the company; you are buying a contract **derived** from the company's price.
    - **Options:** You pay a 'Premium' (fee) to bet on a price move. If you are wrong by a certain date, your money goes to zero.
    - **Futures:** You agree to buy a commodity (like 1,000 barrels of Oil) at a set price in the future. You *must* fulfill this contract, which makes it very risky.
    """)

    st.subheader("📉 Shorting")
    st.write("Borrowing shares to sell them high and buy them back low. You are betting that a company will fail.")
    

with tab5:
    st.header("Page 5: The Execution Process")
    st.write("What does it actually look like to go from 'Information' to 'Ownership'?")

    st.markdown("""
    ### The Sequence of a Trade
    1. **The Portal:** You log into your **Brokerage** (The Gatekeeper).
    2. **The Selection:** You enter the **Ticker Symbol** (e.g., AAPL for Apple or MTNN for MTN Nigeria).
    3. **The Instruction:** You place a **Limit Order**. You tell the broker: 'I want 5 shares at no more than $190.'
    4. **The Match:** The Broker sends your request to the **Exchange** (NYSE or NGX). A seller is found who agrees to your price.
    5. **The Ownership:** The Exchange confirms the trade. You now own the **Shares**. 
    6. **The Clearing:** One business day later (**T+1**), the money and the shares officially 'settle' in the respective accounts.
    """)

    st.divider()
    st.subheader("🌍 Popular Assets to Watch")
    colA, colB = st.columns(2)
    with colA:
        st.write("**US Markets:**")
        st.write("- **Stocks:** Nvidia (NVDA), Tesla (TSLA)")
        st.write("- **ETFs:** VOO (S&P 500), QQQ (Nasdaq 100)")
        st.write("- **Commodities:** Gold, WTI Crude Oil")
    with colB:
        st.write("**Nigerian Markets:**")
        st.write("- **Stocks:** Dangote Cement, Zenith Bank")
        st.write("- **Baskets:** NGX 30 Index")
        st.write("- **Commodities:** Cocoa, Brent Crude")

st.divider()
st.caption("Educational Manual v1.2 | No Financial Advice Provided.")