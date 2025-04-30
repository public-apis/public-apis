import openai
import responses
import os
# Function that makes the API call to OpenAI
openai.api_key=os.getenv("OPENAIAPI")
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Engine is part of the URL
        prompt=prompt,
        max_tokens=50
    )
    # return response['choices'][0]['message']['content'].strip()
    return response.choices[0].text.strip()


@responses.activate
def test_get_openai_response():
    # Mock the OpenAI API response with the correct URL
    responses.add(
        responses.POST,
        'https://api.openai.com/v1/engines/text-davinci-003/completions',  # Full URL including engine
        json={
            'choices': [{'text': 'This is a mocked response'}]
        },
        status=200
    )

    # Call the function that would normally make the OpenAI API call
    result = get_openai_response("Hello, OpenAI!")

    # Assertions to check if the mocked response is returned
    assert result == 'This is a mocked response'
