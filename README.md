# Stacking_Max_Tensile
## Ensemble Machine Learning (Stacked ML)
Because merely one ML model could not provide the best solution, various ML models are integrated to select the suitable ML model well-suited to the input data.
In this study KNearest Neighbors Regressor, SGDRegressor, Decision Tree regressor, Gradient Boost Regressor were used as weak learners and LassoLarsCV was used as meta learner
to combine the results.

## Tree based pipline optimization Techniques(TPOT)
An evolutionary algorithm TPOT was chosen to be used in this study which applies genetic algorithms programming in order to optimize the ML pipelines. A different number of
seeds were utilized in the TPOT code in order to ensure that the accuracy of the developed model was not affected by the selection of the training dataset.

## Autokeras
AutoKeras is an open-source library that automates the process of neural network architecture search, hyperparameter tuning, and model optimization. It is designed to simplify the complex and time-consuming task of manually designing and fine-tuning neural network architectures. AutoKeras is built on top of TensorFlow and Keras, making it easy to integrate into existing deep learning workflows.
 ## ANN
 Ann with 2 hidden layers and Relu as activation function was used for prediction.
