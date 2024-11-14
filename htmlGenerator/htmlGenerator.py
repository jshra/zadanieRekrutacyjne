from openai import OpenAI

client = OpenAI(api_key = '')

textPath = 'text.txt'
articleFile = 'artykul.html'
templateFile = 'szablon.html'
previewFile = 'podglad.html'

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
model = "gpt-4o"
try:
    htmlResponse = client.chat.completions.create(
        model= model,
        messages=[
            {"role": "system", "content": "You are an expert in HTML, webpage design, and image prompt engineering."},
            {"role": "user", "content": (
    "Convert the following text into a structured HTML format. "
    "Use HTML tags only to structure the content with headers, paragraphs, and lists where appropriate. "
    "Insert two to three images at relevant points by including <figure> elements with <img> tags and the attribute src='image_placeholder.jpg'. "
    "For each <img>, add an alt attribute that includes a detailed prompt describing the content of the image for an AI image generator, based on the context of the article. "
    "Include captions for each image using the <figcaption> tag, written in Polish. "
    "Return only the code to go between <body> and </body> tags, excluding the <html>, <head>, and <body> tags. "
    "Additionally, restore any missing Polish characters to the text. "
    "Return the answer without code markdowns. "
    f"Here’s the text: {text}"
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
        if bodyStart and bodyEnd:
            newContent = templateContent[:bodyStart] + htmlCode + templateContent[bodyEnd:]
        else:
            raise Exception("No <body> tag found in template")
        
        with open(previewFile, 'w', encoding='utf-8') as output:
            output.write(newContent)
            
except Exception as e:
    print(e)
    
