# 適合率、再現率、F1
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# データを格納します。今回は0が陰性、1が陽性を示しています
# 常にPositive予測＋偏ったデータ(全部Positive)
# y_true = [1,1,1,1,1,1,1,1,1,1]
# y_pred = [1,1,1,1,1,0,0,0,0,0]
# 常にPositive予測
y_true = [1,1,1,1,1,0,0,0,0,0]
y_pred = [1,1,1,1,1,1,1,1,1,1]
# 常にNegative予測
# y_true = [1,1,1,1,1,0,0,0,0,0]
# y_pred = [0,0,0,0,0,0,0,0,0,0]
# 多めのPositive予測
# y_true = [1,1,1,1,1,0,0,0,0,0]
# y_pred = [1,1,1,1,1,1,1,1,0,0]
# 少な目のPositive予測
# y_true = [1,1,1,1,1,0,0,0,0,0]
# y_pred = [1,1,1,0,0,0,0,0,0,0]
# 完全に予測を外す
# y_true = [1,1,1,1,1,0,0,0,0,0]
# y_pred = [0,0,0,0,0,1,1,1,1,1]
# 完璧な予測
# y_true = [1,1,1,1,1,0,0,0,0,0]
# y_pred = [1,1,1,1,1,0,0,0,0,0]

# 適合率と再現率をあらかじめ計算します
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

# 以下の行にF1スコアの定義式を書いてください
f1_sc = f1_score(y_true, y_pred)
f1_sc_manual = 2 * ( precision * recall ) / ( precision + recall )

print("accuracy:  %.3f" % accuracy)     # 正解率
print("precision: %.3f" % precision)    # 適合率
print("recall:    %.3f" % recall)       # 再現率
print("F1:        %.3f" % f1_sc)        # F1-score
print("F1 manual: %.3f" % f1_sc_manual) # F1-score 手動計算
