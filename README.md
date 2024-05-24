# How Robust are the Tabular QA Models for Scientific Tables? A Study using Customized Dataset [Accepted in LREC-COLING 2024]

## Abstract
Question-answering (QA) on hybrid scientific tabular and textual data deals with scientific information, and relies
on complex numerical reasoning. In recent years, while tabular QA has seen rapid progress, understanding
their robustness on scientific information is lacking due to absence of any benchmark dataset. To investigate the
robustness of the existing state-of-the-art QA models on scientific hybrid tabular data, we propose a new dataset,
“SciTabQA”, consisting of 822 question-answer pairs from scientific tables and their descriptions. With the help of this
dataset, we assess the state-of-the-art Tabular QA models based on their ability (i) to use heterogeneous information
requiring both structured data (table) and unstructured data (text) and (ii) to perform complex scientific reasoning
tasks. In essence, we check the capability of the models to interpret scientific tables and text. Our experiments
show that “SciTabQA” is an innovative dataset to study question-answering over scientific heterogeneous data. We
benchmark three state-of-the-art Tabular QA models, and find that the best F1 score is only 0.462.

## Code and dataset usage

The codes for TAPAS, TAPEX and OmniTab are present in the .ipynb files in the Code folder, they can be used to run evaluation. The Github is being updated.
