# AutoQAPairGen

AutoQAPairGen is a system that generates question-answer pairs from unstructured data (pdf) based on user-defined schemas. This tool allows you to extract structured question-answer pairs by providing a schema, making it easier to process and analyze unstructured data.

## Features
- Generate question-answer pairs based on custom schemas.
- Easily extract structured information from unstructured data.
- Fully open-source and customizable.

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

