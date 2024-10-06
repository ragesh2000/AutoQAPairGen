# AutoQAPairGen

AutoQAPairGen is a system designed to simplify the process of preparing data for fine-tuning machine learning models. It generates question-answer pairs from unstructured data (such as PDFs) based on user-defined schemas. This tool allows you to convert unstructured data into a structured format that aligns with your schema, making it easier to prepare data for training or fine-tuning both language and vision models.

## Features
- Generate question-answer pairs from unstructured data (including PDFs) based on custom schemas.
- Capable of chunking data without losing continuity, ensuring seamless processing of large or complex documents.
- Handles embedded images and includes them in the corresponding data chunks for processing.
- Automatically generates structured question-answer pairs in line with user-defined schemas.
- Fully open-source, customizable, and easily extendable for specific use cases.

## Prerequisites
- GPU support: since we are using the open source model, we need to have a GPU to run the model.
- Python 3.10 or higher.


## Installation

To get started, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/QA-SchemaGen.git
cd QA-SchemaGen
```
### 2. Create a virtual environment
```bash
conda create -n qa-gen python=3.10
conda activate qa-gen
```
### 3. Install the required packages
```bash
pip install -r requirements.txt
```
### 4. Run the application

You can run the application with the following command:

```bash
python run.py  -category <text/vision>
```
*Note: The `-category` is an optional argument to specify whether you are processing data for a language model (text) or a vision model (vision). If not provided, the system will default to processing data for a language model.*

## Usage 
1. Run the application
2. Provide the path for the unstructured data (currently only pdf is supported)
3. Provide the schema for the question-answer pairs (eg: {'user': question, 'bot': answer})
4. The application will generate the question-answer pairs based on the schema

