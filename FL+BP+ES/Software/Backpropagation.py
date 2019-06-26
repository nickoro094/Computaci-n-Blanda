from math import exp
from random import seed
from random import random
from csv import reader
import sys


# Inicializa la red neuronal (in -> hidden -> out)
def initialize_network(n_in, hidden_neur, n_out):
    network = list()
    hidden_layer = [{'weights': [random() for i in range(n_in + 1)]} for i in range(hidden_neur)]
    network.append(hidden_layer)
    output_layer = [{'weights': [random() for i in range(hidden_neur + 1)]} for i in range(n_out)]
    network.append(output_layer)
    return network


def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation


# Funcion de activacion (Sigmoide)
def activ_func(activation):
    return 1.0 / (1.0 + exp(-activation))


# Forward propagate
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = activ_func(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


# Calcula la derivada de la funcion de activacion para las salidas
def activ_func_deriv(output):
    return output * (1.0 - output)


# Actualiza los pesos de la red neuronal con los errores del backtrack
def update_weights(network, row, learn_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += learn_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] += learn_rate * neuron['delta']


# Entrenamiento de la red neuronal n_epoch veces
def train_network(network, train_set, learn_rate, n_epoch, n_out):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train_set:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_out)]
            expected[row[-1]] = 1
            sum_error += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, learn_rate)
        print('>epoch=%d, learning rate=%.3f, error=%.3f' % (epoch, learn_rate, sum_error))


def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))


def defuzzifier(data):
    defuzzy_data = ['0','0']
    if data[3] == 'mala':
        defuzzy_data[0] = 3
    elif data[3] == 'buena':
        defuzzy_data[0] = 1
    elif data[3] == 'regular':
        defuzzy_data[0] = 2

    if data[4] == 'poca':
        defuzzy_data[1] = 1
    elif data[4] == 'mucha':
        defuzzy_data[1] = 3
    elif data[4] == 'moderada':
        defuzzy_data[1] = 2

    return defuzzy_data

def expert_KnwB(riesgo, data):
    p_data = ((data[0] + data[1]) / 2) - 0.2
    final_risk = riesgo * p_data

    if(data[0] and data[1]) == 3:
        final_risk = 70

    if final_risk > 66:
        print('\x1b[1;31;49mPeligro! Transitar con cuidado')
        if data[0] == 3:
            print('\x1b[1;31;49mVelocidad Recomendada: 10- 30 Km/h')
        else:
            print('\x1b[1;31;49mVelocidad Recomendada: 20- 40 Km/h')
    elif final_risk <= 35:
        print('\x1b[1;34;49mEs seguro transitar')
        print('\x1b[1;34;49mVelocidad Recomendada: 45- 90 Km/h')
    else:
        print('\x1b[1;32;49mPrecaucion al transitar')
        print('\x1b[1;32;49mVelocidad Recomendada: 30- 60 Km/h')

# Backpropagate errores y actualizar neuronas
def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * activ_func_deriv(neuron['output'])


# Funcion principal: inicializa red, entrena y predice un dataset = unknwn_data
def back_propagation(train_set, unknwn_data, learn_rate, n_epoch, hidden_neur):
    n_in = len(train_set[0]) - 1
    n_out = len(set([row[-1] for row in train_set]))
    network = initialize_network(n_in, hidden_neur, n_out)
    train_network(network, train_set, learn_rate, n_epoch, n_out)
    predictions = list()
    for row in unknwn_data:
        prediction = predict(network, row)
        predictions.append(prediction)
    return predictions


def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


if __name__ == '__main__':
    seed(1)
    # hora, mes, año, carretera, lluvia, codigo
    data_pick = [['02', 'junio', '2012', 'regular', 'moderada'],
                 ['05', 'enero', '2018', 'mala', 'poca'],
                 ['10', 'enero', '2015', 'buena', 'poca'],
                 ['18', 'febrero', '2017', 'regular', 'mucha'],
                 ['22', 'agosto', '2019', 'mala', 'mucha'],
                 ['20', 'julio', '2019', 'buena', 'mucha']]

    dataset = load_csv('training_set.csv')
    for i in range(len(dataset[0]) - 1):
        str_column_to_float(dataset, i)
    str_column_to_int(dataset, len(dataset[0]) - 1)

    test_set = list()
    for row in dataset:
        row_copy = list(row)
        test_set.append(row_copy)
        row_copy[-1] = None

    i = 0
    accuracy_delta = 0
    predictions = back_propagation(dataset, test_set, 0.3, 200, 5)

    for row in dataset:
        if(row[-1] == predictions[i]):
            #print('\x1b[1;32;49mExpected=%d, Prediction=%d' % (row[-1], predictions[i]))
            accuracy_delta += 1
        else:
            accuracy_delta += 0
            #print('\x1b[1;31;49mExpected=%d, Prediction=%d' % (row[-1], predictions[i]))
        i = i+1

    riesgo = float(((accuracy_delta) * 100) / i)
    error_rn = riesgo * 0.01
    #print('\x1b[1;37;49mPrecision = %f%%' % riesgo)
    for i in data_pick:
        expert_in = defuzzifier(i)
        expert_KnwB(riesgo, expert_in)

    print('\x1b[0mError =', error_rn)



