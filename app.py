import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/KhushiKalra21/Dashboard-of-Import-Export/main/Random_Sample.csv")

# Create labels for charts if needed
df['Label'] = df['Product'] + ': ' + df['Country']
df['Label_Trade'] = df['Import_Export'] + ': ' + df['Product']

# Sidebar for user input
st.sidebar.title("Select Options")

# Dropdown for selection
chart_dropdown = st.sidebar.selectbox(
    'Select Chart Type',
    ['Product Category vs Country (Import/Export)', 'Port vs Shipping Method', 'Bubble Chart', 'Trade Volume by Port', 'Country-wise Product Categories and Payment Terms', 'Country-wise Customs Code Analysis']
)

# Treemap Chart: Product Category vs Country (Import/Export)
if chart_dropdown == 'Product Category vs Country (Import/Export)':
    st.title('Product Category vs Country (Import/Export)')
    selected_trade_type = st.sidebar.selectbox('Select Trade Type', ['Import', 'Export', 'Both'])
    
    if selected_trade_type != 'Both':
        filtered_data = df[df['Import_Export'] == selected_trade_type]
    else:
        filtered_data = df
    
    fig = px.treemap(filtered_data, path=['Country', 'Import_Export', 'Product'],
                     title=f'Product Category vs Country ({selected_trade_type})')
    st.plotly_chart(fig)

# Sunburst Chart 1: Port vs Shipping Method for Product Categories
elif chart_dropdown == 'Port vs Shipping Method':
    st.title('Port vs Shipping Method for Product Categories')
    filtered_data = df
    fig = px.sunburst(filtered_data, path=['Port', 'Shipping_Method', 'Product'],
                      title='Port vs Shipping Method for Product Categories')
    st.plotly_chart(fig)

# Bubble Chart: Quantity vs Value of Trade Transactions
elif chart_dropdown == 'Bubble Chart':
    st.title('Quantity and Payment Method Trade Transactions')
    fig = px.scatter(df, x='Quantity', y='Payment_Terms', size='Payment_Terms', color='Payment_Terms',
                     hover_name='Payment_Terms', title='Quantity  of Trade Transactions',
                     labels={'Quantity': 'Trade Quantity', 'Payment_Terms': 'Payment Method'})
    st.plotly_chart(fig)

# Vertical Bar Chart: Trade Volume by Port (with Shipping Method Differentiation)
elif chart_dropdown == 'Trade Volume by Port':
    st.title('Trade Volume by Port (with Shipping Method Differentiation)')
    filtered_data = df
    fig = px.bar(filtered_data, x='Port', y='Quantity', color='Shipping_Method',
                 title='Trade Volume by Port (with Shipping Method Differentiation)',
                 labels={'Quantity': 'Trade Volume'})
    st.plotly_chart(fig)

# Sunburst Chart 2: Country-wise Product Categories and Payment Terms
elif chart_dropdown == 'Country-wise Product Categories and Payment Terms':
    st.title('Country-wise Product Categories and Payment Terms')
    filtered_data = df
    fig = px.sunburst(filtered_data, path=['Country', 'Product', 'Payment_Terms'],
                      title='Country-wise Product Categories and Payment Terms')
    st.plotly_chart(fig)

# Horizontal Bar Chart: Country-wise Customs Code Analysis for Product Categories
elif chart_dropdown == 'Country-wise Customs Code Analysis':
    st.title('Country-wise Customs Code Analysis for Product Categories')
    filtered_data = df
    fig = px.bar(filtered_data, y='Customs_Code', x='Product', color='Country',
                 title='Country-wise Customs Code Analysis for Product Categories',
                 labels={'Customs_Code': 'Customs Code', 'Product': 'Product Category'},
                 orientation='h')
    st.plotly_chart(fig)
