from data_extraction.web_scraper import scrape_news
from data_extraction.ocr_processing import extract_text_from_image
from data_processing.text_cleaner import clean_text
from data_processing.normalization import normalize_text_data
from vectorization.text_vectorizer import vectorize_text
from script_generation.script_creator import create_script_with_langchain
from avatar_presentation.presentation_adapter import adapt_script_with_langchain
from data_analysis.trend_analysis import analyze_trends
from data_analysis.data_visualization import visualize_data
from data_processing.process_data import generate_structured_data_with_langchain


def main():
    # Step 1: Data Extraction
    print("Extracting news data...")
    # TODO: Use environment variable or argument for URL
    url = "https://example.com"
    raw_articles = scrape_news(url)

    # If scraping fails, fallback to OCR (example image path provided)
    if not raw_articles:
        print("Scraping failed or returned no articles. Falling back to OCR.")
        image_path = "web_new_screenshot.png"
        raw_text = extract_text_from_image(image_path)
        if raw_text:
            raw_articles = [raw_text]
        else:
            print("OCR also failed. Exiting.")
            return

    # Step 2: Data Cleaning and Normalization
    print("Cleaning and normalizing text data...")
    cleaned_articles = [clean_text(article) for article in raw_articles]

    structured_data = generate_structured_data_with_langchain(cleaned_articles)

    normalized_data = [normalize_text_data(data) for data in structured_data]
    print(f"Normalized data: {normalized_data}")

    # Step 3: Vectorization
    print("Vectorizing text data...")
    corpus = [data["content"] for data in normalized_data if data.get("content")]
    vectors, features = None, []
    if corpus:
        vectors, features = vectorize_text(corpus)
        print(f"Vectors shape: {vectors.shape if vectors is not None else 'None'}")
    else:
        print("No content to vectorize.")

    # Step 4: Script Generation
    print("Generating scripts...")
    tone = [
        "Free Market," "Limited Government," "Individual Liberty," "Fiscal Austerity"
    ]
    ideology = [
        "Free Market," "Limited Government," "Individual Liberty," "Fiscal Austerity"
    ]
    scripts = [
        create_script_with_langchain(data, tone=tone, ideology=ideology)
        for data in normalized_data
    ]

    # Step 5: Adapt Scripts for Avatar Presentation
    print("Adapting scripts for avatar presentation...")
    adapted_scripts = [adapt_script_with_langchain(script) for script in scripts]

    # Step 6: Data Analysis
    print("Analyzing trends...")
    if vectors is not None:
        try:
            trend_vector = analyze_trends(vectors.toarray())
            if trend_vector is not None and len(trend_vector) > 0:
                # Map features to trends if features exist
                trends = {}
                if len(features) == len(trend_vector):
                     trends = {features[i]: trend_vector[i] for i in range(len(features))}
                else:
                     trends = {f"Feature {i}": trend for i, trend in enumerate(trend_vector)}

                # Step 7: Data Visualization
                print("Visualizing data...")
                # visualization might block execution in some environments, usually show() blocks
                # We will call it but be aware it opens a window
                visualize_data(trends)
            else:
                 print("Trend vector is empty.")
        except Exception as e:
            print(f"Error analyzing trends: {e}")
    else:
        print("Vectorization failed or no vectors, cannot analyze trends.")

    # Output the results
    print("Final Adapted Scripts for Avatar Presentation:")
    for script in adapted_scripts:
        print(script)


if __name__ == "__main__":
    main()
