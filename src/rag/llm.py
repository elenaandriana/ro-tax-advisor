from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
   

people_prompt = ChatPromptTemplate.from_template(
    """You are a tax advisor. Answer the following question: "

     Context: {context}
     Question: {question}

        Answer:""" ) 
def build_prompt(result, question: str):
    context = "\n\n".join([f"- {item}" for item in result])
    return people_prompt.format(context=context, question=question) 


if __name__ == "__main__":
    result = [
        "The tax rate for individuals is 25%.",
        "You can deduct up to $10,000 in charitable donations.",
        "Capital gains are taxed at a rate of 15%."
    ]
    question = "What is the tax rate for individuals?"
    prompt = build_prompt(result, question)
    print(prompt)