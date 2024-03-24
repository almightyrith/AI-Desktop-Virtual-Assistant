from requests_html import HTMLSession
import speech_to_text  # Assuming this module contains the speech_to_text function you provided

# Function to fetch weather information for a specific location using Google search
def weather():
    s = HTMLSession()
    query = "patna"  # Example location, replace with the desired location
    url = f'https://www.google.com/search?q=weather+{query}'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

    # Send a GET request to the weather URL with the specified User-Agent header
    r = s.get(url, headers={'User-Agent': user_agent})

    # Extract weather information from the HTML response
    temperature = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    description = r.html.find('span#wob_dc', first=True).text

    # Concatenate temperature, unit, and description into a single string and return
    return f"{temperature} {unit} {description}"