import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LogisticRegression

# leer los datos, IMPORTANTE poner su ruta de archivo...
data = pd.read_csv("E:/Work/Disco D/Kevin/Universidad/Inteligencia artificial/Actividades/diabetes_data.csv")

print("data: ", data)

# Separar características y etiquetas
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Escalar características
sc = StandardScaler()
X = sc.fit_transform(X)

# dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# crear el clasificador
classifier = LogisticRegression(random_state=0)

# entrenar el modelo
classifier.fit(X_train, y_train)

# hacer predicciones en el conjunto de prueba
y_pred = classifier.predict(X_test)

# calcular la precisión del modelo
accuracy = classifier.score(X_test, y_test)
print("Precisión del modelo:", accuracy)

# crear un nuevo conjunto de datos
new_data = np.array([[50, 1, 25, 1.5, 125]])

# escalar las características
new_data = sc.transform(new_data)

# hacer la predicción
prediction = classifier.predict(new_data)

# imprimir la predicción
if prediction == 1:
    print("El paciente tiene diabetes.")
else:
    print("El paciente no tiene diabetes.")