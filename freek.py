from flask import send_file, render_template
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/Sales_April_2019_visualisatie.csv')

def genereer_grafiek():
    df_plot = df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False)
    plt.bar(df_plot.index, df_plot.values, zorder=3)
    plt.title('April 2019 - Aantal verkocht per product')
    plt.grid(axis='y')
    plt.xticks(rotation=90)
    bestands_pad = 'static/grafieken/totale_sales_april_2019.png'
    plt.savefig(bestands_pad)
    return send_file(bestands_pad, mimetype='image/png')

def toon_totale_sales():
    return render_template('image.html', bestands_pad='static/grafieken/totale_sales_april_2019.png')
