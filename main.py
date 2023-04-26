# this is the main file for the project
import openai

# call openai completion API


def generate_responses(
    prompt,
    num_outputs
):
    import openai

    openai.api_key = "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"

    responses = openai.Completion.create(
        model="davinci:ft-personal:immigration-finetune-2023-04-17-13-40-11",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=num_outputs)

    return cleanup(responses)

# a bunch of helper functions


def cleanup(responses):
    return [response["text"].strip() for response in responses["choices"]]

# display the responses in order


def plot_responses(responses):
    for response in responses:
        print(response)

# function to ask terminal for input


def ask(prompt):
    return input(prompt)

# send input to openai


def send_input_to_openai(input):
    return generate_responses(input, 1)

# get continuous input from terminal


def get_input():
    while True:
        input = ask("Question: ")
        response = send_input_to_openai(input)
        print(response)

# pdf to text


def pdf_to_text(file):
    import PyPDF2
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    return text

# input file to text


def input_file_to_text(file):
    with open(file, 'r') as f:
        return f.read()

# text from file to openai


def text_to_openai(text):
    return generate_responses(text, 1)

# connect file to text to openai continuous input


def file_to_openai(file):
    text = pdf_to_text(file)
    text = "give tips on how to fill out form \n" + text
    return text_to_openai(text)


# input to choose whether to call get_input or file_to_openai
resp = ask("Do you want to ask a question or upload a file? (q/f) ")
if resp == "q":
    get_input()
else:
    ans = ask("What is the file name? ")
    api_resp = file_to_openai(ans)
    print(api_resp)

