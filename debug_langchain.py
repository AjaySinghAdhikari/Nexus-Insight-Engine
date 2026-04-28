import sys
print("Starting imports")
try:
    print("Importing dotenv")
    from dotenv import load_dotenv
    print("Importing langchain_groq")
    from langchain_groq import ChatGroq
    print("Importing langchain_core.prompts")
    from langchain_core.prompts import ChatPromptTemplate
    print("Importing langchain_core.output_parsers")
    from langchain_core.output_parsers import JsonOutputParser
    print("Done importing all")
except Exception as e:
    print("Error:", e)
print("Finished script")
