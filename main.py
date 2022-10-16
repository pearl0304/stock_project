# pip install pandas
# pip install matplotlib
# pip install plotly
# pip install lxml
# pip install requests

import matplotlib.pyplot as plt
import plotly.express as px
from stock import get_daily_stock_info_by_company

company = '삼성전자'
df = get_daily_stock_info_by_company(company)

## 단순 차트 그리기
plt.figure(figsize=(10,4))
plt.plot(df['date'], df['close'])
plt.xlabel('')
plt.ylabel('close')
plt.tick_params(
    axis='x',
    which='both',
    bottom=False,
    top=False,
    labelbottom=False)
plt.savefig(company + ".png")
plt.show()


## 반응형 차트 그리기
fig = px.line(df, x='date', y='close', title='{}의 종가(close) Time Series'.format(company))

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.show()
fig.write_html("file.html")