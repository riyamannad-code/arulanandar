import google.generativeai as genai
genai.configure(api_key="AIzaSyB5H_bUuwomSkkFS-GgmBuxig3N9kZ8BuY")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)
