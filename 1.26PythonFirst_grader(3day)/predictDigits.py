# 画像ファイルから数字を予測するプログラム
import sklearn.datasets
import sklearn.svm #SVMのために必要
import PIL.Image #画像を扱うために必要
import numpy #配列を扱うために必要

# 画像ファイルを数値データに変換する
def imageToData(filename):
    # 画像を8x8のグレースケールに変換し、数字の配列に変換する
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS) #PIL.Image.Resampling.LANCZOSは画像を8x8に変換する
    # 数値リストに変換
    numImage = numpy.asarray(grayImage, dtype=float) # assarrayは配列を作成する関数. dtype=floatは配列の要素の型を指定する
    numImage = 16 - numpy.floor(16 * (numImage / 256)) #### 行列の各要素を計算. floorは小数点以下を切捨. 
    ####256で割るのは0~1の範囲にするため. 16をかけるのは0~16の範囲にするため
    numImage = numImage.flatten() # 一次元に変換. flattenは配列を一次元に変換する関数
    
    return numImage # 数値リストを返す

# 数字を予測する
def predictDigits(data): # dataは数値リスト
    # 学習用データを読み込む
    digits = sklearn.datasets.load_digits() #データセットを読み込む
    # 機械学習する
    clf = sklearn.svm.SVC(gamma=0.001) #機械学習のアルゴリズムを指定. SVCはサポートベクターマシン. gammaはパラメータ
    clf.fit(digits.data, digits.target) #機械学習する. dataは画像データ, targetはラベル
    # 予測結果を表示する
    n = clf.predict([data]) # 予測する. dataは数値リスト
    print("判定結果=", n) # 結果を表示する

# 画像ファイルを数値リストに変換する
data = imageToData("8-3.jpg") # 画像ファイルを指定する
# 数字を予測する
predictDigits(data) # 数字を予測する
