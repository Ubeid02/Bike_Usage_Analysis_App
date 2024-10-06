import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Load cleaned combined_bike_sharing_data.csv
df = pd.read_csv("combined_bike_sharing_data.csv")

# Konversi kolom 'dteday' menjadi tipe datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Dashboard Header
st.header('Bike Sharing Dashboard')

# Sidebar Filter by Date Range
min_date = df['dteday'].min()
max_date = df['dteday'].max()

with st.sidebar:
    st.image("../data/images (2).jpeg")
    start_date, end_date = st.date_input(
        label='Filter by Date Range',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data berdasarkan rentang tanggal
filtered_df = df[(df['dteday'] >= pd.to_datetime(start_date)) & (df['dteday'] <= pd.to_datetime(end_date))]

# Pertanyaan 1: Penggunaan Sepeda Berdasarkan Hari Kerja dan Akhir Pekan
st.subheader("Bike Rentals: Weekday vs Weekend")

weekday_vs_weekend = filtered_df.groupby('workingday')['cnt'].sum().reset_index()
weekday_vs_weekend['day_type'] = weekday_vs_weekend['workingday'].apply(lambda x: 'Weekday' if x == 1 else 'Weekend')

# Menampilkan nilai total penyewaan untuk Weekday dan Weekend
weekday_total = weekday_vs_weekend[weekday_vs_weekend['day_type'] == 'Weekday']['cnt'].values[0]
weekend_total = weekday_vs_weekend[weekday_vs_weekend['day_type'] == 'Weekend']['cnt'].values[0]
ratio = weekday_total / weekend_total

st.write(f"Total Bike Rentals on Weekdays: **{weekday_total}**")
st.write(f"Total Bike Rentals on Weekends: **{weekend_total}**")
st.write(f"Ratio of Weekday to Weekend Rentals: **{ratio:.2f}**")

# Visualisasi: Weekday vs Weekend
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='day_type', y='cnt', data=weekday_vs_weekend, ax=ax)
ax.set_title("Total Bike Rentals: Weekday vs Weekend", fontsize=14)
ax.set_xlabel('Day Type')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

# Pertanyaan 2: Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari (hour.csv)
st.subheader("Bike Rentals per Hour of the Day")

hourly_rentals = filtered_df.groupby('hr')['cnt'].mean().reset_index()

# Menampilkan nilai rata-rata dan median untuk penyewaan per jam
hourly_mean = hourly_rentals['cnt'].mean()
hourly_median = hourly_rentals['cnt'].median()

st.write(f"Mean of Bike Rentals per Hour: **{hourly_mean:.2f}**")
st.write(f"Median of Bike Rentals per Hour: **{hourly_median:.2f}**")

# Visualisasi: Line Chart untuk Penyewaan Sepeda per Jam
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hourly_rentals, marker='o', ax=ax)
ax.set_title("Average Bike Rentals by Hour", fontsize=14)
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Average Rentals')
st.pyplot(fig)

# RFM Analysis: Frequency and Recency
st.subheader("RFM Analysis: Frequency and Recency")

# Menghitung Frequency
frequency_df = filtered_df.groupby(['casual', 'registered'])['cnt'].sum().reset_index()

# Membuat kolom untuk User Type
frequency_df['User Type'] = frequency_df.apply(lambda row: 'Casual' if row['casual'] > 0 else 'Registered', axis=1)

# Menghitung Recency
last_rentals = filtered_df.groupby(['casual', 'registered'])['dteday'].max().reset_index()
last_rentals['Recency'] = (filtered_df['dteday'].max() - last_rentals['dteday']).dt.days

# Menggabungkan Frequency dan Recency
rfm_df = frequency_df.merge(last_rentals[['casual', 'registered', 'Recency']], on=['casual', 'registered'])

# Menampilkan nilai rata-rata Frequency dan Recency
avg_frequency = rfm_df['cnt'].mean()
avg_recency = rfm_df['Recency'].mean()

st.write(f"Average Frequency of Rentals: **{avg_frequency:.2f}**")
st.write(f"Average Recency (Days Since Last Rental): **{avg_recency:.2f}**")

# Visualisasi Frequency menggunakan Boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='User Type', y='cnt', data=rfm_df, ax=ax)
ax.set_title('Distribution of Frequency of Bike Rentals by User Type', fontsize=14, pad=20)
ax.set_xlabel('User Type', fontsize=12)
ax.set_ylabel('Total Frequency of Rentals', fontsize=12)
st.pyplot(fig)

# Visualisasi Recency menggunakan Boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='User Type', y='Recency', data=rfm_df, ax=ax)
ax.set_title('Recency of Bike Rentals by User Type', fontsize=14, pad=20)
ax.set_xlabel('User Type', fontsize=12)
ax.set_ylabel('Recency (Days Since Last Rental)', fontsize=12)
st.pyplot(fig)

st.caption('Copyright (c) 2023 Bike Sharing Data Dashboard')
