import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
pio.renderers.default = 'browser'
import numpy as np
import pydeck as pdk
import webbrowser

st.title("🦠 COVID-19 DASHBOARD");
st.sidebar.markdown("# NAVIGATION")
options = st.sidebar.radio("Choose different page from the below menu:",("COVID-19 - India","COVID-19 - World", "Useful Links & Sources", "Prevent from COVID-19","Donate to Charity",));
st.sidebar.markdown("# ABOUT")
st.sidebar.info("Hey! Nice of you to come here :smile: Let me know if you liked this little experiment. If you find any bugs or need any more information. Ping Me: \n\nTelegram: **💬 @rajeshkumaar**\n\n **📧 rajeshkumaracet@gmail.com**")
st.sidebar.info("**Data Sources:** Johns Hopkins University (GitHub) & covid19india.")
st.sidebar.warning("**Disclaimer:** The illustrations provided by using covid19india & Johns Hopkins University datasets only.")
orginal_data = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv");
state_wise = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv", index_col="State"); 
get_data = state_wise['Last_Updated_Time'][0];
#Donate to charity page
if options == "Donate to Charity":
    st.warning("Hi, We all are aware of the pandemic situation due to spread of Corona Virus. This has lead to lockdown in many countries and states. India is no exception for it. Pondicherry is one state where lockdown has impacted many homeless people. More than 2000 homeless people are struggling for everyday needs.\n\nNo Waste Food In Pondy works towards providing homeless people with daily essential things like bedsheets, plates with tumblers and other needy things along with dry ration. It costs ₹ 500 per head for the essentials. This is a small initiative to help people who are in need. We would be grateful if you could provide your help by donating for the noble cause.")

    st.success("**For more Information:**\n\nName: **Jainraj Ejoumal**\n\nPh.No: **+91 9597333633**\n\n**You also donate us using Paytm, GooglePay, PhonePay & also directly to Bank Account:**\n\n Paytm:  **+91 9597333633**\n\nGoogle Pay: **+91 9597333633**\n\nPhonePe: **+91 9597333633**\n\nAccount Name : **No Waste Food In Pondy** \n\nAccount No : **920020007494708**\n\nBank Name : **Axis Bank**\n\nIFSC : **UTIB0002694**")

    st.warning('"_When people were hungry, God didn’t say, “Now is that political, or social?” He said, “I feed you.” Because the good news to a hungry person is bread._" - Desmond Tutu')

    st.markdown("<p style='text-align:center'><b style='color:#f40552'> #Say No to Hunger, 💗 from Pondicherry</p>",unsafe_allow_html=True)

# txt = f"Today is March {date}."

if options == "COVID-19 - India":
    st.success("Hi👋! A cool COVID-19 Visualization, for getting actionable insights. Use the sidebar for switching different pages.")

    st.markdown(f"<div style='display:flex;justify-content:flex-end;'><p style='background-color:#05386b;padding:7px;border-radius:50px;color:white'>🕒 Last updated: {get_data} <p></div>",unsafe_allow_html=True)

     #Fig3
    remove_row = orginal_data.drop(0)
    fig3 = go.Figure(data=[go.Table(header=dict(values=orginal_data.columns[:5]),
                 cells=dict(values=[remove_row["State"],remove_row["Confirmed"],remove_row["Recovered"], remove_row["Deaths"], remove_row["Active"]], align='left', font_size=12,
    height=40)) ])
    fig3.update_layout(title_text='COVID-19 Cases in Different States in India:',width=800, height=600)             
    st.write(fig3)

    #Fig1
    a = state_wise.iloc[0, [0,1,2,3,]].to_frame()
    b = a["Total"].tolist()
    res = [str(x) + ('k') for i, x in enumerate(b)]
    labels=['Confirmed', 'Recovered', 'Deaths', "Active"]
    fig1 = go.Figure([go.Bar(x=labels, y=b,text=res,
            textposition='outside')])
    fig1.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=5, opacity=0.6)
    fig1.update_layout(title_text='COVID-19 Cases in India:', width=800, height=500)
    st.write(fig1)

    #Fig2
    fig2 = go.Figure(data=[
    go.Bar(name='Confirmed',x=orginal_data["State"].drop(0).to_numpy(), y=orginal_data["Confirmed"].drop(0).to_numpy()),
    go.Bar(name='Recovered',x=orginal_data["State"].drop(0).to_numpy(), y=orginal_data["Recovered"].drop(0).to_numpy()),
    go.Bar(name="Deaths", x=orginal_data["State"].drop(0).to_numpy(), y=orginal_data["Deaths"].drop(0).to_numpy()),
    go.Bar(name="Active", x=orginal_data["State"].drop(0).to_numpy(), y=orginal_data["Active"].drop(0).to_numpy()),
    ])

    fig2.update_layout(barmode='relative', width=800, height=600,xaxis={'categoryorder':'total descending'})
    st.write(fig2)
   

    
    fig4 = px.scatter(remove_row, x="Confirmed", y="Recovered", color="State",
                 size='Confirmed', hover_data=['Confirmed', "Recovered", "Deaths"])
    fig4.update_layout(title_text='Confirmed Vs Recovered Cases Vs Deaths:',width=800, height=600)
    st.write(fig4)

    st.subheader("**COVID -19 cases at Different Dates:**");
    time_series = pd.read_csv("https://api.covid19india.org/csv/latest/case_time_series.csv");
    fig5 = px.line(time_series, x = "Date", y ="Daily Confirmed" )
    fig5.add_scatter(x=time_series['Date'], y=time_series['Daily Recovered'], mode='lines',  name="Daily Recovered")
    fig5.add_scatter(x=time_series['Date'], y=time_series['Daily Deceased'], mode='lines', name="Daily Deceased")
    fig5.update_xaxes(rangeslider_visible=True);
    fig5.update_layout(width=800, height=600)  
    st.write(fig5)


    fig6 = px.line(time_series, x = "Date", y ="Total Confirmed" )
    fig6.add_scatter(x=time_series['Date'], y=time_series['Total Recovered'], mode='lines',  name="Total Recovered")
    fig6.add_scatter(x=time_series['Date'], y=time_series['Total Deceased'], mode='lines', name="Total Deceased")
    fig6.update_layout(width=800, height=600)  
    fig6.update_xaxes(rangeslider_visible=True)
    st.write(fig6)
    
    st.subheader("**Choose State from Choose State from below Select for more detail insight:**")
    get_state = st.selectbox("Choose a State:",remove_row["State"].to_numpy());
    district_wise = pd.read_csv("https://api.covid19india.org/csv/latest/district_wise.csv");
    for_filter = district_wise.loc[district_wise["State"] == get_state][:-1]
    fig7 = go.Figure(data=[
    go.Bar(name='Active',x=for_filter["District"].to_numpy(), y=for_filter["Active"].to_numpy()),
    go.Bar(name='Recovered',x=for_filter["District"].to_numpy(), y=for_filter["Recovered"].to_numpy()),
    go.Bar(name="Decreased", x=for_filter["District"].to_numpy(), y=for_filter["Deceased"].to_numpy())
    ])
    fig7.update_layout(barmode='relative', width=800, height=600,xaxis={'categoryorder':'total descending'})
    st.write(fig7)

    fig8 = px.scatter(for_filter, x="Active", y="Recovered", color="District",
                 size='Confirmed', hover_data=['Confirmed', "Recovered", "Deceased"])
    fig8.update_layout(width=800, height=600,xaxis={'categoryorder':'total descending'})
    st.write(fig8)
    

if options == "Useful Links & Sources":
    st.info("**🔗 Some Cool Resources to get upto date on COVID-19: (India)**")
    sources = pd.read_csv("https://api.covid19india.org/csv/latest/sources_list.csv",index_col="Region").replace(np.nan, "-", regex=True)
    a= sources[['Source_1', 'Source_2']]
    st.table(a)

if options == "Prevent from COVID-19":
    st.header("**Download Aarogya Setu Mobile Application: (India)**")
    st.info("**Aarogya Setu**, an app using Bluetooth range as a proximity sensor under which the user can be infected by another Covid-19 positive patient. When two smartphones with the app installed in them come in each other's Bluetooth range the app will exchange information. If one of the user is positive, the other person will be alerted about possibility of being infected. These potential cases are then notified to government for further testing.")
    st.write("**Click the below button to download the App:**")
    if st.button('🚀For ios'):
         webbrowser.open_new_tab("https://apps.apple.com/in/app/aarogyasetu/id1505825357")
    if st.button("🚀 For Andriod"):
        webbrowser.open_new_tab("https://play.google.com/store/apps/details?id=nic.goi.aarogyasetu&hl=en_IN")
    st.subheader("6 Steps To Prevent from COVID-19")
    st.markdown('<iframe width="700" height="400" src="https://www.youtube.com/embed/9Ay4u7OYOhA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.markdown("**Source:** CDC")
    st.subheader("What Coronavirus Symptoms Look Like, Day By Day")
    st.markdown('<iframe width="700" height="400" src="https://www.youtube.com/embed/OOJqHPfG7pA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.markdown("**Source:** Science Insider")
    st.subheader("COVID-19 Animation: What Happens If You Get Coronavirus?")
    st.markdown('<iframe width="700" height="400" src="https://www.youtube.com/embed/5DGwOJXSxqg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.markdown("**Source:** Nucleus Medical Media")
    st.markdown("<p style='text-align:center;background-color:#6497b1 ; color:white; padding:10px; border-radius:50px'>🏠 Stay Home & Save Lives 🙏</p>",unsafe_allow_html=True)
if options == "COVID-19 - World":
    countries = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-03-2020.csv");
    get_only_countries = countries = countries.iloc[3017:]
    fig9 = go.Figure(data=[
    go.Bar(name='Confirmed',x=countries["Country_Region"].to_numpy(), y=countries["Confirmed"].to_numpy())
    ])
    fig9.update_layout(title_text='Confirmed cases Around the Countries:',barmode='relative', width=900, height=600,xaxis={'categoryorder':'total descending'})
    st.write(fig9)

    fig10 = go.Figure(data=[
    go.Bar(name='Recovered',x=countries["Country_Region"].to_numpy(), y=countries["Recovered"].to_numpy())
    ])
    fig10.update_layout(title_text='Recovered cases Around the Countries:',barmode='relative', width=900, height=600,xaxis={'categoryorder':'total descending'})
    st.write(fig10)

    fig11 = go.Figure(data=[
    go.Bar(name="Deaths", x=countries["Country_Region"].to_numpy(), y=countries["Deaths"].to_numpy())])
    fig11.update_layout(title_text='Deaths cases Around the Countries:',barmode='relative', width=900, height=600,xaxis={'categoryorder':'total descending'})
    st.write(fig11)
     
    fig12 = go.Figure(data=[
    go.Bar(name="Active", x=countries["Country_Region"].to_numpy(), y=countries["Active"].to_numpy())])
    fig12.update_layout(title_text='Active cases Around the Countries:',barmode='relative', width=900, height=600,xaxis={'categoryorder':'total descending'})
    st.write(fig12)
    
    fig13 = go.Figure(data=[
    go.Bar(name='Confirmed',x=countries["Country_Region"].to_numpy(), y=countries["Confirmed"].to_numpy()),
    go.Bar(name='Recovered',x=countries["Country_Region"].to_numpy(), y=countries["Recovered"].to_numpy()),
    go.Bar(name="Deaths", x=countries["Country_Region"].to_numpy(), y=countries["Deaths"].to_numpy()),
    go.Bar(name="Active", x=countries["Country_Region"].to_numpy(), y=countries["Active"].to_numpy())
    ])

    fig13.update_layout(barmode='relative', width=900, height=600,xaxis={'categoryorder':'total descending'})
    st.write(fig13)

    fig14 = px.scatter(countries, x="Confirmed", y="Recovered", color="Country_Region",
                 size='Confirmed', hover_data=['Confirmed', "Recovered", "Deaths", "Active"])
    fig14.update_layout(title_text='Confirmed Vs Recovered Cases Vs Deaths Vs Active:',width=900, height=600)
    st.write(fig14)

    # aaaa = get_only_countries[["Long_", "Lat"]]    
   

#     layer = pdk.Layer(
#     "HexagonLayer",
#     data=a.dropna(),
#     get_position="[lng, lat]",
#     auto_highlight=True,
#     elevation_scale=50,
#     pickable=True,
#     elevation_range=[0, 3000],
#     extruded=True,
#     coverage=1,
#     )

# # Set the viewport location
#     view_state = pdk.ViewState(
#     longitude=-1.415, latitude=52.2323, zoom=6, min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36
#     )

# # Combined all of it and render a viewport
#     r = pdk.Deck(
#     map_style="mapbox://styles/mapbox/light-v9",
#     layers=[layer],
#     initial_view_state=view_state,
#     tooltip={"html": "<b>Elevation Value:</b> {elevationValue}", "style": {"color": "white"}},
#     )
#     st.pydeck_chart(r)



    #deck gl
    # df = countries[['Long_','Lat']]
    

    # st.pydeck_chart(pdk.Deck(
    # map_style='mapbox://styles/mapbox/light-v9',
    #  initial_view_state=pdk.ViewState(
    #     latitude=37.76,
    #     longitude=-122.4,
    #     zoom=11,
    #     pitch=50,
    #  ),
    # layers=[pdk.Layer(
    #     'HexagonLayer',
    #      data=aaaa,
    #         get_position='[Long_, Lat]',
    #         radius=200,
    #         elevation_scale=4,
    #         elevation_range=[0, 1000],
    #         pickable=True,
    #         extruded=True,
    #     ),
    #      pdk.Layer('ScatterplotLayer',        
    #       data=aaaa,
    #         get_position='[Long_, Lat]',
    #         get_color='[200, 30, 0, 160]',
    #          get_radius=200,
    #      ),
    # ],
    # ))


 




    