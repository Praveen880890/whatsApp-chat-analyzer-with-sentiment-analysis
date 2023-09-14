# Table of Contents

1. [WhatsApp Chat Analyzer with Sentiment Analysis](#whatsapp-chat-analyzer-with-sentiment-analysis)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [How to Use](#usage)
5. [Sentiment Analysis Model](#sentiment-analysis-model-1)
6. [Data Preprocessing](#data-preprocessing-1)
7. [Note](#note)
8. [Acknowledgments](#acknowledgments-1)
9. [Disclaimer](#disclaimer)
10. [Demo](#demo) 

# WhatsApp Chat Analyzer with Sentiment Analysis

WhatsApp Chat Analyzer is a Python application for analyzing and visualizing WhatsApp chat data. This application allows you to upload your WhatsApp chat history and gain insights into various aspects of your chat, including statistics, sentiment analysis, word cloud, emoji analysis, and more.

## Features

- **Statistics**: Provides an overview of the chat, including the total number of messages, words, media messages, and links shared.

- **Sentiment Analysis**: Analyzes the sentiment of the chat, categorizing it as Very Negative, Negative, Neutral, Positive, or Very Positive.

- **Monthly Timeline**: Displays a timeline of messages sent each month.

- **Daily Timeline**: Shows a timeline of messages sent each day.

- **Activity Map**: Visualizes the activity levels of users in the group.

- **Most Busy Users**: Identifies the most active users in the group.

- **Word Cloud**: Generates a word cloud visualization of the most commonly used words.

- **Most Common Words**: Lists the most frequently used words in the chat.

- **Emoji Analysis**: Analyzes the usage of emojis in the chat.

- **Download Guide**: Provides a step-by-step guide on how to download your WhatsApp chat history for analysis.

## Prerequisites

Before running the WhatsApp Chat Analyzer, make sure you have the following libraries installed:

- Streamlit
- Matplotlib
- Seaborn
- Numpy
- Pandas
- Pillow (PIL)
- Wordcloud
- Emoji
- Transformers (Hugging Face Transformers library)

You can install these libraries using `pip`:

```bash
pip install streamlit matplotlib seaborn numpy pandas pillow wordcloud emoji transformers
```

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Run the Application**: Open your terminal and navigate to the project folder. Run the Streamlit application using the following command:

   ```bash
   streamlit run app.py
   ```

3. **Upload WhatsApp Chat**: Click on the "Choose a file" button in the sidebar to upload your WhatsApp chat text file.

4. **Select User**: Choose the user whose chat analysis you want to view or select "Overall" for group-level analysis.

5. **Click "Show Analysis"**: After selecting the user, click the "Show Analysis" button to initiate the analysis process.

6. **Explore the Results**: Explore various analysis sections such as statistics, sentiment analysis, timelines, activity maps, and more.

7. **Download Chat**: If you're unsure how to download your WhatsApp chat, click on the "Know about it" button in the sidebar to view a step-by-step guide.

## Sentiment Analysis Model

The sentiment analysis in this application is powered by the "nlptown/bert-base-multilingual-uncased-sentiment" model from the Hugging Face Transformers library. This model assigns sentiment scores to messages, categorizing them as Very Negative, Negative, Neutral, Positive, or Very Positive.

## Data Preprocessing

The application includes a data preprocessing step to extract user names, messages, and relevant timestamps from the WhatsApp chat text file. It also performs various data transformations to prepare the data for analysis.

## Note

- This application is designed for educational and personal use.

- Ensure that your WhatsApp chat text file is in a compatible format for analysis.

- The application may take some time to analyze large chat histories.

- Some features like the word cloud and emoji analysis may not work properly with non-English chats.


## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/) for the sentiment analysis model.
- [Streamlit](https://streamlit.io/) for the interactive web application framework.

---

Enjoy analyzing your WhatsApp chats with sentiment analysis using the WhatsApp Chat Analyzer! If you have any questions or suggestions, feel free to reach out.

**Disclaimer**: This application is not affiliated with WhatsApp and is intended for personal use only.

## Demo 
https://praveen880890-whatsapp-chat-analyzer-with-sentiment--app-u3qync.streamlit.app/
