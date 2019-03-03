import numpy as np 
import cv2, pickle
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt 

data_file = './png-etl1/katakana.pickle'
im_size = 25
out_size = 46
im_color = 1
in_shape = (im_size, im_size, im_color)

data = pickle.load(open(data_file, 'rb'))

y = []
x = []

for d in data:
    (num, img) = d
    img = img.astype('float').reshape(im_size, im_size, im_color) / 255
    y.append(keras.utils.np_utils.to_categorical(num, out_size))
    x.append(img)
x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

model = Sequential()
model.add(Conv2D(
    32,
    kernel_size=(3, 3),
    activation='relu',
    input_shape=in_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(out_size, activation='softmax'))
model.compile(
    loss='categorical_crossentropy', 
    optimizer=RMSprop(), 
    metrics=['accuracy']
)

hist = model.fit(
    x_train, 
    y_train, 
    batch_size=128, 
    epochs=12,
    verbose=1, 
    validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=1)
print('acc:', score[1], ' loss:', score[0])

plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('accuracy')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Loss')
plt.legend(['train', 'test'], loc='upper left')
plt.show()