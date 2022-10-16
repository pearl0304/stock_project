import pandas as pd


def get_stock_code(company):
  KRX_code = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

  ## 최신 상장순으로 정렬
  KRX_code = KRX_code.sort_values(['상장일'], ascending=False)

  ## 필요한 칼럼만 가져오기
  KRX_code = KRX_code[['회사명', '종목코드']]

  ## 컬럼명 영어로 바꾸기
  KRX_code = KRX_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

  ## 종목코드 6자리로 포맷 맞추기
  KRX_code['code'] = KRX_code['code'].map('{:06d}'.format)

  code = KRX_code[KRX_code['company'] == company]['code'].values[0].strip()
  return code
