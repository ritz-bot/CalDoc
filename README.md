# CalDoc

## Overview

**CalDoc** is a health-focused application that helps users monitor their dietary intake by analyzing the nutritional content and calorie count of their meals. By simply uploading a picture of your food, the app utilizes Google's Gemini Pro Vision API to provide detailed information about the food items, including calorie count, nutritional balance, and an overall assessment of the meal's healthiness.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Methods and Requirements](#methods-and-requirements)
  - [Environment Setup](#environment-setup)
  - [Functions](#functions)
  - [API Key and Libraries](#api-key-and-libraries)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Image-Based Calorie Counting**: Upload a photo of your meal, and get a breakdown of the calories for each item.
- **Nutritional Analysis**: Assess whether the food is healthy based on its nutritional content.
- **Detailed Reporting**: Provides information on the proportion of carbohydrates, fats, fibers, and other nutrients.
- **Interactive UI**: Simple and user-friendly interface using Streamlit for quick meal assessments.

## Installation

To set up the Calorie Advisor application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ritz-bot/calorie-advisor.git
    cd calorie-advisor
    ```

2. **Create a virtual environment**:
    ```bash
    conda create -n calorie-advisor python=3.10
    conda activate calorie-advisor
    ```

3. **Install required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API key**:
    - Obtain a Google Gemini Pro API key from [Google's Maker Suite](https://makersuite.google.com/).
    - Create a `.env` file in the root directory with the following content:
    ```bash
    GOOGLE_API_KEY=your_google_api_key
    ```

5. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Start the application**:
    - Run the command `streamlit run app.py` in your terminal.
    - A browser window should open with the application interface.

2. **Upload a food image**:
    - Click the "Choose an image" button to upload a picture of your meal.

3. **Get calorie information**:
    - Click the "Tell me about the calories" button.
    - The application will display the calorie count, nutritional analysis, and health assessment of the meal.

## Methods and Requirements

### Environment Setup

1. **Virtual Environment Creation**:
    - The application requires Python 3.10 for compatibility with the Google Gemini Pro API.
    - Use `conda create -n calorie-advisor python=3.10` to set up a conda environment.

2. **Install Dependencies**:
    - Dependencies include Streamlit for the front-end interface, the Google Generative AI library for interacting with the API, and `python-dotenv` for managing environment variables.

### Functions

#### `get_gemini_response(input_prompt, image)`

This function interacts with the Google Gemini Pro Vision API to generate a response based on the input prompt and image data.

- **Parameters**:
  - `input_prompt`: A prompt specifying the information to extract from the image.
  - `image`: The image data in a format that the API can process.
- **Returns**: A string with the API's response containing calorie and nutritional information.

#### `input_image_setup(uploaded_file)`

This function processes the uploaded image file, extracting the image data required by the API.

- **Parameters**:
  - `uploaded_file`: The file object of the uploaded image.
- **Returns**: The image data formatted for API use, including MIME type and binary data.

### API Key and Libraries

1. **API Key**:
    - Obtain from [Google's Maker Suite](https://makersuite.google.com/).
    - Store in a `.env` file to keep it secure.

2. **Libraries**:
    - **Streamlit**: For creating the user interface.
    - **Google Generative AI**: For integrating with Google Gemini Pro Vision API.
    - **python-dotenv**: For loading environment variables from a `.env` file.

### Front-End Setup

- **Header**: Displays the app name "CalDoc".
- **Image Upload**: Allows users to upload images of their food.
- **Submit Button**: Processes the uploaded image and displays the calorie and nutritional information.

### Sample Input and Output

- **Input**: An image of a meal (e.g., a plate of chicken biryani).
- **Output**: Detailed breakdown of calories, nutritional balance, and health assessment.

## Contributing

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature/your-feature`).
3. **Commit your changes** (`git commit -m 'Add some feature'`).
4. **Push to the branch** (`git push origin feature/your-feature`).
5. **Open a Pull Request**.


![Xnip2024-06-26_00-59-20](https://github.com/ritz-bot/CalDoc/assets/55766032/20a27107-8930-4bce-b58c-182658d5582e)
