# python-pro

## 仮想環境の作成
 * python -m venv env

## plotlyのインストール
 * pip install plotly

## dashのインストール
 * pip install dash

## CPU プロファイリング
 * python -m cProfile --sort cumtime xxxxx.py
 → percall、cumtimeの大きなものを探し出すことで「容疑者」を特定する

## 実行時間の計測
 * timeit → python -m timeit xxxxxx.py

## ユニットテストの実行
 * python -m unittest

## pytestのインストール
 * pip install pytest

## pytestの実行
 * pytest
 * pytestのテストケースの作成ルール
 * * クラス名を Test* として作成する 

 ## Requestsのインストール(https://github.com/psf/requests)
  * pip install requests