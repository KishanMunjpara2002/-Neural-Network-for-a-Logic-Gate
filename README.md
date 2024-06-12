---

# Logic Gate Neural Network Visualizer

This project provides an interactive interface to visualize the decision boundaries and confusion matrices of neural networks trained to model different logic gates (AND, OR, XOR, NAND, NOR, XNOR). The visualizer is built using Gradio and uses Matplotlib and Scikit-learn for plotting and modeling.

## Features

- **Interactive Visualization**: Adjust hyperparameters such as the number of hidden units, learning rate, and maximum iterations to see how they affect the model's performance.
- **Logic Gates**: Visualize decision boundaries for AND, OR, XOR, NAND, NOR, and XNOR gates.
- **Confusion Matrix**: See the confusion matrix to understand the model's performance on the training data.

## Requirements

- Python 3.6 or higher
- Gradio
- NumPy
- Matplotlib
- Scikit-learn

## Installation


1. Install the required packages:

   ```bash
   pip install numpy matplotlib scikit-learn gradio
   ```

## Logic Gate Parameters

For each logic gate, you can use the following recommended hyperparameter values to achieve expected results:

1. **AND Gate**:
   - **Hidden Units**: 2
   - **Learning Rate**: 0.01
   - **Max Iterations**: 10000

2. **OR Gate**:
   - **Hidden Units**: 2
   - **Learning Rate**: 0.01
   - **Max Iterations**: 10000

3. **XOR Gate**:
   - **Hidden Units**: 5
   - **Learning Rate**: 0.01
   - **Max Iterations**: 20000

4. **NAND Gate**:
   - **Hidden Units**: 2
   - **Learning Rate**: 0.01
   - **Max Iterations**: 10000

5. **NOR Gate**:
   - **Hidden Units**: 2
   - **Learning Rate**: 0.01
   - **Max Iterations**: 10000

6. **XNOR Gate**:
   - **Hidden Units**: 5
   - **Learning Rate**: 0.01
   - **Max Iterations**: 20000

## Example

Here is an example of how to visualize the XOR gate:

1. Run the script:
   ```bash
   python logic_gate_visualization.py
   ```
2. In the web interface, set the parameters:
   - **Logic Gate**: XOR
   - **Hidden Units**: 5
   - **Learning Rate**: 0.01
   - **Max Iterations**: 20000

3. Observe the decision boundary and confusion matrix for the XOR gate.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Gradio](https://gradio.app/)
- [Scikit-learn](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)

---

This README file provides all necessary details about the project, including how to install dependencies, run the script, and expected values for specific logic gates.
