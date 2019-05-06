import numpy as np 
import cv2, pickle
from sklearn.model_selection import train_test_split
import keras

data_file = './png-etl1/katakana.pickle'
im_size = 25
in_size = im_size * im_size
out_size = 46

data = pickle.load(open(data_file, 'rb'))

y = []
x = []
for d in data:
    (num, img) = d
    img = img.reshape(-1).astype('float') / 255
    y.append(keras.utils.np_utils.to_categorical(num, out_size))
    x.append(img)
x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

Dense = keras.layers.Dense
model = keras.models.Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size, )))
model.add(Dense(out_size, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.fit(
    x_train, 
    y_train, 
    batch_size=20, 
    epochs=50, 
    verbose=1, 
    validation_data=(x_test, y_test)
)

score = model.evaluate(x_test, y_test, verbose=1)
print('acc:', score[1], '.  loss:', score[0])