from flask import Flask, render_template, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import io
from io import BytesIO

plt.style.use('ggplot')



app =  Flask(__name__)

@app.route("/tables")
def show_tabes():
    data = pd.read_csv('Dataset.csv')
    return render_template('Webinterface.html', tables = data.to_html(), titles = 'Monthly rain falling data from 1965-2018')


@app.route("/data_visualise")
def data_visualise():
    data = pd.read_csv('Dataset.csv')
    new_data_jan = data.get('January')
    new_data_feb = data.get('Feb')
    new_data_mar = data['March']
    new_data_apr = data.get('April')

    new_data1 = data['year']


    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
  #  fig.suptitle('Graphs in order- Jan-Feb-Mar-Apr')
    ax1.plot(new_data1, new_data_jan)
    ax1.set_xlabel('Year')
    ax1.set_title("January")
    ax1.set_ylabel("rainfall(mm)")

    ax2.plot(new_data1, new_data_mar)
    ax2.set_xlabel('Year')
    ax2.set_title("February")
    ax2.set_ylabel("rainfall(mm)")

    ax3.plot(new_data1, new_data_feb)
    ax3.set_xlabel('Year')
    ax3.set_title("March")
    ax3.set_ylabel("rainfall(mm)")

    ax4.plot(new_data1, new_data_apr)
    ax4.set_xlabel('Year')
    ax4.set_title("April")
    ax4.set_ylabel("rainfall(mm)")
    plt.tight_layout()

    canvas = FigureCanvas(fig)
    img1 = BytesIO()
    fig.savefig(img1)
    img1.seek(0)
    return send_file(img1, mimetype='image/png')



@app.route('/visulization')
def visulization():
    return render_template('visulization.html')


if __name__ =="__main__":
    app.run(debug=True)


