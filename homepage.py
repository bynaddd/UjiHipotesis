import streamlit as st
import numpy as np
from scipy import stats

st.title('WEBSITE UJI HIPOTESIS')

with st.sidebar:
    tipe = st.radio('Pilih Tipe', ['Uji hipotesis rata-rata 1 populasi', 'Uji hipotesis rata-rata 2 populasi', 'Uji hipotesis rata-rata K populasi'
    , 'Uji hipotesis varians 1 populasi', 'Uji hipotesis varians 2 populasi', 'Uji hipotesis proporsi 1 populasi'
    ,'Uji hipotesis proporsi 2 populasi',])

# Uji hipotesis 1 populasi
if tipe == 'Uji hipotesis rata-rata 1 populasi':
    st.header('Uji Hipotesis Rata-Rata 1 Populasi')
    st.subheader('Masukkan Data')
    data = st.text_input('Masukkan data (pisahkan dengan koma)', '1, 2, 3, 4, 5')
    data = [float(x.strip()) for x in data.split(',')]

    # Melakukan uji hipotesis
    st.subheader('Uji Hipotesis')
    mean_h0 = st.number_input('H0 ∶μ=', value=0.0)
    mean_h1 = st.number_input('H1 ∶μ=', value=1.0)
    alpha = st.number_input('Tingkat signifikansi (alpha)', value=0.05)

    t_stat, p_value = stats.ttest_1samp(data, mean_h0)

    st.write('T-statistik:', t_stat)
    st.write('Nilai p:', p_value)

    # Menampilkan kesimpulan uji hipotesis
    if p_value < alpha:
        st.write('Kesimpulan: Tolak H0')
    else:
        st.write('Kesimpulan: Terima H0')

# Uji hipotesis 2 populasi
elif tipe == 'Uji hipotesis rata-rata 2 populasi':
    st.header('Uji Hipotesis Rata-Rata 2 Populasi')
    st.subheader('Masukkan Data')
    data1 = st.text_input('Masukkan data populasi 1 (pisahkan dengan koma)', '1, 2, 3, 4, 5')
    data1 = [float(x.strip()) for x in data1.split(',')]

    data2 = st.text_input('Masukkan data populasi 2 (pisahkan dengan koma)', '1, 2, 3, 4, 5')
    data2 = [float(x.strip()) for x in data2.split(',')]

    # Melakukan uji hipotesis
    st.subheader('Uji Hipotesis')
    mean_h0 = st.number_input('H0 ∶μ1-μ2=', value=0.0)
    mean_h1 = st.number_input('H1 ∶μ1-μ2=', value=1.0)
    alpha = st.number_input('Tingkat signifikansi (alpha)', value=0.05)

    t_stat, p_value = stats.ttest_ind(data1, data2)

    st.write('T-statistik:', t_stat)
    st.write('Nilai p:', p_value)

    # Menampilkan kesimpulan uji hipotesis
    if p_value < alpha:
        st.write('Kesimpulan: Tolak H0')
    else:
        st.write('Kesimpulan: Terima H0')

# Uji hipotesis k populasi
elif tipe == 'Uji hipotesis rata-rata K populasi':
    st.header('Uji Hipotesis Rata-Rata K Populasi')
    st.subheader('Masukkan Data')
    k = st.number_input('Jumlah populasi (k)', value=2, min_value=2, step=1)

    data = []
    for i in range(k):
        data_input = st.text_input(f'Masukkan data populasi {i+1} (pisahkan dengan koma)', '1, 2, 3, 4, 5')
        data_input = [float(x.strip()) for x in data_input.split(',')]
        data.append(data_input)

    # Melakukan uji hipotesis
    st.subheader('Uji Hipotesis')
    alpha = st.number_input('Tingkat signifikansi (alpha)', value=0.05)

    f_stat, p_value = stats.f_oneway(*data)

    st.write('F-statistik:', f_stat)
    st.write('Nilai p:', p_value)

    # Menampilkan kesimpulan uji hipotesis
    if p_value < alpha:
        st.write('Kesimpulan: Tolak H0')
    else:
        st.write('Kesimpulan: Terima H0')

elif tipe == 'Uji hipotesis varians 1 populasi':
    st.header('Uji Hipotesis Varians 1 Populasi')
    st.subheader('Masukkan Data')
    data = st.text_input('Masukkan data (pisahkan dengan koma)', '1, 2, 3, 4, 5')
    data = [float(x.strip()) for x in data.split(',')]

    # Melakukan uji hipotesis
    st.subheader('Uji Hipotesis')
    var_h0 = st.number_input('H0 : Varians =      ', value=1.0)
    var_h1 = st.number_input('H1 : Varians ≠  σ    ', value=2.0)
    alpha = st.number_input('Tingkat signifikansi (alpha)', value=0.05)

    n = len(data)
    var_sample = np.var(data, ddof=1)
    f_stat = var_sample / var_h0
    p_value = 1 - stats.f.cdf(f_stat, n - 1, n - 1)

    st.write('F-statistik:', f_stat)
    st.write('Nilai p:', p_value)

    # Menampilkan kesimpulan uji hipotesis
    if p_value < alpha:
        st.write('Kesimpulan: Tolak H0')
    else:
        st.write('Kesimpulan: Terima H0')

# Uji hipotesis varians 2 populasi
elif tipe == 'Uji hipotesis varians 2 populasi':
    st.header('Uji Hipotesis Varians 2 Populasi')
    st.subheader('Masukkan Data')
    data1 = st.text_input('Masukkan data populasi 1 (pisahkan dengan koma)', '1, 2, 3, 4, 5')
    data1 = [float(x.strip()) for x in data1.split(',')]

    data2 = st.text_input('Masukkan data populasi 2 (pisahkan dengan koma)', '1, 2, 3, 4, 5')
    data2 = [float(x.strip()) for x in data2.split(',')]

    # Melakukan uji hipotesis
    st.subheader('Uji Hipotesis')
    var_h0 = st.number_input('H0 : varians populasi 1 - varians populasi 2 =', value=1.0)
    var_h1 = st.number_input('H1 : varians populasi 1 - varians populasi 2 ≠ ', value=2.0)
    alpha = st.number_input('Tingkat signifikansi (alpha)', value=0.05)

    n1 = len(data1)
    n2 = len(data2)
    var1 = np.var(data1, ddof=1)
    var2 = np.var(data2, ddof=1)
    f_stat = var1 / var2
    p_value = 1 - stats.f.cdf(f_stat, n1 - 1, n2 - 1)

    st.write('F-statistik:', f_stat)
    st.write('P Value:', p_value)

    # Menampilkan kesimpulan uji hipotesis
    if p_value < alpha:
        st.write('Kesimpulan: Tolak H0')
    else:
        st.write('Kesimpulan: Terima H0')


# Uji hipotesis proporsi 1 populasi
elif tipe == 'Uji hipotesis proporsi 1 populasi':
    st.header('Uji Hipotesis Proporsi 1 Populasi')
    st.subheader('Masukkan Data')
    x = st.number_input('Jumlah keberhasilan (x)', value=10, min_value=0, step=1)
    n = st.number_input('Jumlah percobaan (n)', value=100, min_value=1, step=1)

    # Melakukan uji hipotesis
    st.subheader('Uji Hipotesis')
    p_h0 = st.number_input('H0: 𝑝 =  ', value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    alpha = st.number_input('Tingkat signifikansi (alpha)', value=0.05)

    p_hat = x / n
    z_stat = (p_hat - p_h0) / np.sqrt(p_h0 * (1 - p_h0) / n)
    p_value = 2 * (1 - stats.norm.cdf(np.abs(z_stat)))

    st.write('Z-statistik:', z_stat)
    st.write('Nilai p:', p_value)

    # Menampilkan kesimpulan uji hipotesis
    if p_value < alpha:
        st.write('Kesimpulan: Tolak H0')
    else:
        st.write('Kesimpulan: Terima H0')

elif tipe == 'Uji hipotesis proporsi 2 populasi':
    st.header('Uji Hipotesis Proporsi 2 Populasi')
    st.subheader('Masukkan Data')
    x1 = st.number_input('Jumlah keberhasilan populasi 1 (x1)', value=10, min_value=0, step=1)
    n1 = st.number_input('Jumlah percobaan populasi 1 (n1)', value=100, min_value=1, step=1)

    x2 = st.number_input('Jumlah keberhasilan populasi 2 (x2)', value=15, min_value=0, step=1)
    n2 = st.number_input('Jumlah percobaan populasi 2 (n2)', value=100, min_value=1, step=1)
    alpha = st.number_input('Tingkat signifikansi (alpha)', value=0.05)
    st.write('H0: P1 - P2 =')
    p1_p2 = st.number_input('H1: P1 -P2 ≠ ', value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    

    # Melakukan uji hipotesis
    st.subheader('Hasil Uji Hipotesis')
    p1_hat = x1 / n1
    p2_hat = x2 / n2
    p_hat = (x1 + x2) / (n1 + n2)
    z_stat = ((p1_hat - p2_hat) - (p1_p2 )) / np.sqrt(p_hat * (1 - p_hat) * ((1 / n1) + (1 / n2)))
    p_value = 2 * (1 - stats.norm.cdf(np.abs(z_stat)))

    st.write('Z-statistik:', z_stat)
    st.write('Nilai p:', p_value)

    # Menampilkan kesimpulan uji hipotesis
    if p_value < alpha:
        st.write('Kesimpulan: Tolak H0')
    else:
        st.write('Kesimpulan: Terima H0')

