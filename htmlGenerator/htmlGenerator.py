from openai import OpenAI

client = OpenAI(api_key = '')

textPath = 'text.txt'
articleFile = 'artykul.html'
templateFile = 'szablon.html'
previewFile = 'podglad.html'

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
model = "gpt-4o-mini"
try:
    htmlResponse = client.chat.completions.create(
        model= model,
        messages=[
            {"role": "system", "content": "You are an expert in HTML, webpage design, and image prompt engineering."},
            {"role": "user", "content": (
                "Convert the following text into a structured HTML format. "
                "Use HTML tags only for structure. "
                "Add images where suitable by inserting figures with <img> tag with attribute src='image_placeholder.jpg'. "
                "Include between two and three images. "
                "Add captions to those images using <figcaption> tag. "
                "Additionally, replace the alt text for each image with a detailed prompt for an AI image generator, based on the figcaption and the text. "
                "Return only the code to go between <body> and </body> tags and exclude those tags from answer "
                "Exclude <html>, <head> and <body> tags from the response. "
                "Additionally, restore any missing Polish characters to the text. "
                "Return the answer without code markdowns. "
                f"Here’s the text:{text}"
            )}
        ]
    )
    htmlCode = htmlResponse.choices[0].message.content

    with open(articleFile, 'w', encoding='utf-8') as file:
        file.write(htmlCode)
        
    with open(templateFile, 'r', encoding='utf-8') as template:
        templateContent = template.read()
        bodyStart = templateContent.find("<body>") + len("<body>")
        bodyEnd = templateContent.find("</body>")
        newContent = templateContent[:bodyStart] + htmlCode + templateContent[bodyEnd:]
        
        with open(previewFile, 'w', encoding='utf-8') as output:
            output.write(newContent)
            
except Exception as e:
    print(e)
    
