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
    url = "url_to_scrape"  # Replace with a real news site URL
    raw_articles = scrape_news(url)

    # If scraping fails, fallback to OCR (example image path provided)
    if not raw_articles:
        print("Scraping failed. Falling back to OCR.")
        image_path = "web_new_screenshot.png"  # Replace with a real image path
        raw_text = extract_text_from_image(image_path)
    
    raw_articles = [raw_text]
    
    # Step 2: Data Cleaning and Normalization
    print("Cleaning and normalizing text data...")
    cleaned_articles = [clean_text(article) for article in raw_articles]
    print(cleaned_articles)
    
    structured_data = generate_structured_data_with_langchain(cleaned_articles)
    print(structured_data)
    # structured_data = [{'title': '- Vice Governor of Rio Negro Suspended, Investigation Commission to be Opened', 'content': '- The provincial legislature has decided to suspend Gloria Ruiz, the Vice Governor of Rio Negro, due to moral unfitness. The deputies will now investigate if there was any corruption involved.', 'source': '- Example Source'}]
    normalized_data = [normalize_text_data(data) for data in structured_data]
    
    # Step 3: Vectorization
    print("Vectorizing text data...")
    corpus = [data["content"] for data in normalized_data]
    vectors, features = vectorize_text(corpus)
    
    # Step 4: Script Generation
    print("Generating scripts...")
    tone = "formal"
    ideology = "neutral"
    scripts = [create_script_with_langchain(data, tone=tone, ideology=ideology) for data in normalized_data]
        
    # Step 5: Adapt Scripts for Avatar Presentation
    print("Adapting scripts for avatar presentation...")
    adapted_scripts = [adapt_script_with_langchain(script) for script in scripts]
     
    # Step 6: Data Analysis
    print("Analyzing trends...")
    if vectors is not None:
        trend_vector = analyze_trends(vectors.toarray())
        trends = {f"Feature {i}": trend for i, trend in enumerate(trend_vector)}
        # Step 7: Data Visualization
        print("Visualizing data...")
        visualize_data(trends)
    else:
        print("Vectorization failed, cannot analyze trends.")

    # Output the results
    print("Final Adapted Scripts for Avatar Presentation:")
    for script in adapted_scripts:
        print(script)

if __name__ == "__main__":
    main()
