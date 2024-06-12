import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import gradio as gr
import os

# Function to train the model and plot the decision boundary and confusion matrix
def plot_logic_gate(gate, hidden_units, learning_rate, max_iter):
    # Define the input pairs
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    # Define the output for each logic gate
    outputs = {
        'AND': np.array([0, 0, 0, 1]),
        'OR': np.array([0, 1, 1, 1]),
        'XOR': np.array([0, 1, 1, 0]),
        'NAND': np.array([1, 1, 1, 0]),
        'NOR': np.array([1, 0, 0, 0]),
        'XNOR': np.array([1, 0, 0, 1])
    }

    y = outputs[gate]

    # Train the model
    model = MLPClassifier(hidden_layer_sizes=(hidden_units,), activation='relu', solver='adam', 
                          learning_rate_init=learning_rate, max_iter=max_iter)
    model.fit(X, y)
    y_pred = model.predict(X)

    # Plot decision boundary
    xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 100), np.linspace(-0.5, 1.5, 100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(12, 6))

    # Plot decision boundary
    plt.subplot(1, 2, 1)
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Spectral)
    plt.title(f'{gate} Gate Decision Boundary\nHidden Units: {hidden_units}, Learning Rate: {learning_rate}, Max Iter: {max_iter}')
    plt.xlabel('Input 1')
    plt.ylabel('Input 2')

    # Plot confusion matrix
    plt.subplot(1, 2, 2)
    cm = confusion_matrix(y, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1])
    disp.plot(cmap=plt.cm.Blues, ax=plt.gca())
    plt.title('Confusion Matrix')

    # Save the combined plot to a file
    plot_path = "combined_plot.png"
    plt.savefig(plot_path)
    plt.close()  # Close the figure to prevent it from displaying in non-Gradio environments.
    
    return plot_path

# Gradio interface
interface = gr.Interface(
    fn=plot_logic_gate,
    inputs=[
        gr.Dropdown(choices=['AND', 'OR', 'XOR', 'NAND', 'NOR', 'XNOR'], label="Logic Gate"),
        gr.Slider(1, 10, step=1, value=2, label="Hidden Units"),
        gr.Slider(0.001, 0.1, step=0.001, value=0.01, label="Learning Rate"),
        gr.Slider(1000, 20000, step=500, value=10000, label="Max Iterations")
    ],
    outputs=gr.Image(type="filepath"),
    live=True
)

interface.launch()

interface.launch(share=True)
