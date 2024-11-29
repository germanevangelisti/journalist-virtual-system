# Journalist Virtual System

## Overview

The Journalist Virtual System is an automated platform designed to process and present news through a virtual journalist. It leverages advanced language models to generate and adapt news scripts for virtual avatar presentations.

## Features

- **Data Extraction:** Scrape news articles from websites or extract text from images using OCR.
- **Data Cleaning and Normalization:** Clean and standardize text data for further processing.
- **Script Generation:** Generate news scripts using OpenAI's GPT models.
- **Avatar Presentation:** Adapt scripts for virtual avatar delivery with appropriate pauses and emphasis.
- **Data Visualization:** Visualize trends and data insights using charts.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/journalist_virtual_system.git
   cd journalist_virtual_system
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. **Run the Main Script:**

   ```bash
   python3 main.py
   ```

2. **Customize Script Generation:**

   Modify the `tone` and `ideology` parameters in `main.py` to customize the generated scripts.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.