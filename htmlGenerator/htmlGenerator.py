from openai import OpenAI
client = OpenAI(api_key = '')

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

htmlResponse = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",
         "content": "You are an expert in HTML and webpage design"},
        {"role": "user", "content": (
                "Convert the following text into a structured HTML format. "
                "Use HTML tags only for structure."
                "Add images where suitable by inserting <img> tag with attribute src='image_placeholder.jpg'"
                "Include at least two images"
                "Add captions to those images using suitable HTML tag "
                "Return only the code to go between <body> and </body>"
                "Exclude <html>, <head>, <body> tags from the response."
                "Additionally, restore any missing Polish characters to the text. "
                "Return the answer without code markdowns"
                f"Here’s the text:{text}"
                
            )}
    ]
)
cleanedHtml = htmlResponse.choices[0].message.content.strip()

imagePromptResponse = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",
         "content": "You are an expert in prompt engineering for image generator AIs"},
        {"role": "user", "content": (
                'Make changes in the following html code based on the folowing description'
                'In this html code there are images with alt and figcaption tags connected to them'
                'I want you to replace the text in alt tags with a full prompt for image generator AI'
                'The prompt should be based on both the figcaption and the text'
                'Do not include any other changes to the text'
                'Return only the html code but without code markdowns'
                f'Here’s the text:{cleanedHtml}'
            )}
    ]
)
finalHtml = imagePromptResponse.choices[0].message.content.strip()


with open('artykul.html', 'w', encoding='utf-8') as file:
    file.write(finalHtml)
