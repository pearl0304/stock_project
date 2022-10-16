import requests
import pandas as pd
from krx import get_stock_code


def get_daily_stock_info_by_company(company):
  code = get_stock_code(company)

  # https://www.useragentstring.com/ 에서 user-agent 값 확인하기
  header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

  df = pd.DataFrame()

  for page in range(1, 21):
    url = f"https://finance.naver.com/item/sise_day.naver?code={code}&page={page}"
    res = requests.get(url, headers=header)
    result = pd.read_html(res.text, header=0)[0]
    ## '날짜' 칼럼이 NaN 인 행은 삭제하기
    result = result.dropna(subset=['날짜'])
    df = pd.concat([df, result])

  ## 칼럼명 영어로 수정
  df = df.rename(
    columns={'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})

  ## 데이터 타입 바꾸기
  df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[
    ['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)
  df['date'] = pd.to_datetime(df['date'])

  ## 일자별로 오름 차순 정렬
  df = df.sort_values('date', ascending=True)

  return df
