import numpy as np
# ПЕРЦЕПТРОН
# Функция активации
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# тренировочные данные

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T
# Т транспонировать для того чтобы было 4 на 1
# Инициализация весов
#np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1
# вес синопса не может быть меньше -1 и не может быть больше 1
print("Случайные инициализирующие веса:")
print(synaptic_weights)

# МЕТОД ОБРАТНОГО РАСПОСТРАНЕНИЯ
for i in range(20000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer,synaptic_weights))

    err = training_outputs - outputs
    adjustments = np.dot(input_layer.T,err * (outputs*(1-outputs)))

    synaptic_weights += adjustments

print("Веса после обучения:")
print(synaptic_weights)
print("Результаты после обучения:")
print(outputs)

# Новая ситуация
new_inputs = np.array([1,1,0])
output = sigmoid(np.dot(new_inputs,synaptic_weights))

print("Новая ситуация")
print(output)