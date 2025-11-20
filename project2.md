Project 2: Optimizing Deep Learning Pipelines
Purpose: To enhance your understanding of deep neural network performance by applying various optimization techniques. This project focuses on improving accuracy and generalization using architectural, regularization, and training optimizations.

Skills Used: Python programming, Keras/TensorFlow, Model Optimization, Regularization, Evaluation

Knowledge Goals: Learn how dropout, batch normalization, weight decay, and optimizer choice affect model training and performance.

Summary
In this project, you will experiment with multiple optimization techniques to improve performance on a neural network trained on Sign Language MNIST, a 24-class grayscale image dataset. You will:

Apply regularization techniques such as Dropout, Batch Normalization, and L2 Regularization

Compare at least two optimizers (e.g., Adam, SGD, RMSProp)

Analyze how these optimizations impact training stability and generalization

Visualize results and write a reflective comparison

Repository
You will complete this project using Google Colab. Ensure your notebook is shared privately with the professor and TAs.

Before submission, make sure all cells have been executed and all plots/outputs are visible.

Be sure to add a README.md with instructions for a user trying to clone your repo and a requirements.yml that allows for setup of the Anaconda virtual environment. All required libraries should be present.

Part 1: Experiment Design
 

Your notebook should follow this structure:

Data Loading and Preprocessing
Load Sign Language MNIST
Normalize and reshape inputs
Exploration and Visualization
Plot class distribution
Display representative images
Baseline Model
Simple dense model with 3 layers using Adam optimizer
Train for 5+ epochs with no optimizations
Optimized Models
Implement 3 optimizers (Adam, SGD, RMSProp)
Add Dropout, Batch Normalization, or L2 Regularization
Compare model performance
Evaluation and Visualization
Accuracy/loss curves
Confusion matrix
Classification reports
Summary comparison table
Reflection
Analyze optimizer and regularization impacts
Identify hardest classes to classify
Propose further improvements
Ethical Reflection (optional)
Reflect on accessibility, fairness, or risks of misclassification
Part 2: Experiment Implementation
Inputs:
Use the Sign Language MNIST dataset from Kaggle (24 classes, no 'J' or 'Z')

https://www.kaggle.com/datasets/datamunge/sign-language-mnistLinks to an external site.
 

Exploration and Visualization:
Create a plot class distribution visualization
Display representative images of the dataset.
Comment on each of these.
Anything extra is seen as going above and beyond!
 

Baseline Model:
Create a dense model using Adam optimizer

Train for 5+ epochs with validation_split=0.2

Baseline model should have 3 layers (including final layer):

First layer: 256 neurons

Second layer: 128 neurons

Output layer: 24 neurons (softmax)

Use ReLU activation (or justify an alternative choice)

 

Optimizations:
Create 3 optimized models — one for each optimizer:

Adam (default)

SGD

RMSProp

Implement at least two of the following in at least one model:

Dropout (e.g., Dropout(0.3))

Batch Normalization (e.g., BatchNormalization() after dense layers)

L2 Regularization (e.g., Dense(..., kernel_regularizer=l2(0.001)))

Optimized models should also have 3 layers (not counting Dropout):

First layer: 512 neurons

Second layer: 256 neurons

Output layer: 24 neurons (softmax)

Train each model for 5–20 epochs with validation_split=0.2

 

You are encouraged to experiment with longer training and observe tradeoffs. The goal is experimentation to try to achieve the best results possible.

Evaluation:
Use the following metrics and visualizations:

Training and validation accuracy/loss curves

Confusion matrix heatmap (use seaborn)

Classification report (accuracy, precision, recall, F1-score)

Markdown summary table of all evaluation metrics

Reflection:
In markdown, answer:

How did the optimized models compare to the baseline model?

Which optimization method had the biggest impact and why?

How did the optimizer choice affect performance and learning stability?

Which classes were hardest to classify and why?

What would you change or try next?

Are optimizations like dropout or L2 regularization always beneficial? Why or why not?

Set yourself a challenge: can you get one model to exceed 75% test accuracy? If so, how?
 

Use evidence from your plots and results to justify your answers.

 

Ethical Reflection Prompt (Pick one):

Accessibility and Inclusion

How could deep learning for sign language recognition support or harm accessibility for Deaf and Hard-of-Hearing communities? What ethical responsibilities come with designing such systems?

 

Bias in Model Performance

What are the risks if model optimizations disproportionately benefit some classes (e.g., certain signs) but consistently underperform on others? How can we detect and mitigate this kind of model bias?

 

Over-Optimization and Misuse

Could aggressive optimization of a model lead to harmful unintended consequences (e.g., misuse, overconfidence in deployment, misinterpretation of gestures)? Where should we draw the line between performance and caution?
Part 3: Code Structure Requirements
Notebook Organization:
One .ipynb file containing all code, charts, and reflections

Additional .py files allowed for utility functions

Data folder: if any extrnal dat is used, place all dataset-related files inside a folder called data/

Well-commented code

Markdown explanations of each technique

A markdown "README" cell at the top explaining how to run the notebook

All charts and outputs should be visible in final notebook

Ensure there is a button to open your project in Google Colab.
Linting (optional): You may check formatting with black or flake8 if downloaded.

Deliverable
Submit the Github repo URL. Be sure the repo is set to private and there is a Google Colab button.

Extra Credit (+10 max)
Use a second dataset (e.g., MNIST, SVHN, or your own) and apply the same optimization comparison. Add markdown to compare the performance between datasets.