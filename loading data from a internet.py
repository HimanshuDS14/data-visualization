import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def grapg_data(stock):

    stock_price_url = 'htts://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    







    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("data from stock")
    plt.legend()
    plt.show()



if __name__ == '__main__':
    grapg_data('TSLA')