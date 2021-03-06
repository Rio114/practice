# coding: utf-8
import sys
sys.path.append('..')
import matplotlib.pyplot as plt
import numpy as np
from common.optimizer import SGD
from dataset import ptb
from simple_rnnlm import SimpleRnnlm
import tensorflow as tf


# ハイパーパラメータの設定
batch_size = 10
wordvec_size = 100
hidden_size = 100
time_size = 5  # Truncated BPTTの展開する時間サイズ
lr = 0.1
max_epoch = 100

# 学習データの読み込み（データセットを小さくする）
corpus, word_to_id, id_to_word = ptb.load_data('train')
corpus_size = 1000
corpus = corpus[:corpus_size]
vocab_size = int(max(corpus) + 1)

xs = corpus[:-1]  # 入力 (999)
ts = corpus[1:]  # 出力（教師ラベル）(999)
data_size = len(xs) # 999
print('corpus size: %d, vocabulary size: %d' % (corpus_size, vocab_size))

# 学習時に使用する変数
max_iters = data_size // (batch_size * time_size)
time_idx = 0
total_loss = 0
loss_count = 0
ppl_list = []

# モデルの生成
model = SimpleRnnlm(vocab_size, wordvec_size, hidden_size)
optimizer = SGD(lr)

# ミニバッチの各サンプルの読み込み開始位置を計算
jump = (corpus_size - 1) // batch_size # 1000 // 10 = 100
offsets = [i * jump for i in range(batch_size)] # 100, 200, 300,,,,

for epoch in range(max_epoch):
    for iter in range(max_iters):
        # ミニバッチの取得 # (10, 5)
        # batch_x = tf.Variable(tf.zeros((batch_size, time_size), dtype='int32'))
        # batch_t = tf.Variable(tf.zeros((batch_size, time_size), dtype='int32'))
        batch_x = np.zeros((batch_size, time_size))
        batch_t = np.zeros((batch_size, time_size))

        for i, offset in enumerate(offsets):
            start_slice = offset % data_size # i00 % 999 = i00
            end_slice = start_slice + time_size # i00 + 5
            batch_x[i] = xs[start_slice : end_slice]
            batch_t[i] = ts[start_slice : end_slice]
                # batch_x[i, t] = xs[(offset + time_idx) % data_size]
                # batch_t[i, t] = ts[(offset + time_idx) % data_size]
            # time_idx += 1

        # 勾配を求め、パラメータを更新
        batch_x = tf.constant(batch_x, dtype='int32')
        batch_t = tf.constant(batch_t, dtype='int32')
        loss = model.forward(batch_x, batch_t)
        model.backward()
        optimizer.update(model.params, model.grads)
        total_loss += loss
        loss_count += 1

    # エポックごとにパープレキシティの評価
    ppl = tf.math.exp(total_loss / loss_count)
    print('| epoch %d | perplexity %.2f'
          % (epoch+1, ppl))
    ppl_list.append(float(ppl))
    total_loss, loss_count = 0, 0

# グラフの描画
x = np.arange(len(ppl_list))
plt.plot(x, ppl_list, label='train')
plt.xlabel('epochs')
plt.ylabel('perplexity')
plt.show()
