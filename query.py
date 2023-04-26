# call openai Completion API
def generate_responses(
    prompt,
    num_outputs
):
    import openai

    openai.api_key = "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"

    responses = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=num_outputs)

    return cleanup(responses)

# generate response but specific model


def generate_responses_specific_model(
    prompt,
    num_outputs,
    model_name
):
    import openai

    openai.api_key = "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"

    responses = openai.Completion.create(
        model=model_name,
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
