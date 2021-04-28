import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from datetime import timedelta

data = pd.read_csv('train/train/train.csv', header = 0, parse_dates=True)

# csv 파일 불러오기

data.isnull().sum()

# 결측치 존재유무 확인 -> 확인결과 없었음.

data.info()

# 데이터 타입 확인 -> int와 float로 구성.

data['T'].astype('float64')

# T의 데이터 타입을 float로 변경




