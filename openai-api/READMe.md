# OpenAI API overview

### API Options for text generation
- Chat Completion
- Text Completion

### Other API feature

All these have separate endpoint in the openAI.

- Image generation
- Audio Transcription
- File parsing for fine tuning
- Embedding
- Content Moderation.
  
### What can we do with this OpenAI API
- Summarization
- Chat AI
- Translation
- Data Extraction
- Classification, Categorization, and Sentiment Analysis
- More...

### Sample Chat Completion

Three major params:
1. Model - Text model for use (e.g) (gpt-3.5-turbo)
2. Max Tokens - Max no of words for response. It quits as and when the response breaches it quits immediately.
3. Temperature - No from 0 to 2, changes the variance in responses.

```bash
curl https://api.openai.com/v1/chat/completions   -H "Content-Type: application/json"   -H "Authorization: Bearer $OPENAI_API_KEY"   -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
## Response 
  "id": "cmpl-99ArPEUWhyHe2yrlKtpT2xSlI2lNN",
  "object": "text_completion",
  "created": 1711973727,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": "\n\nIt depends on the situation.",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 7,
    "completion_tokens": 7,
    "total_tokens": 14
  }
}

```

### Sample completion

```bash
## Request
 curl https://api.openai.com/v1/completions   -H "Content-Type: application/json"   -H "Authorization: Bearer $OPENAI_API_KEY"   -d '{
    "model": "gpt-3.5-turbo-instruct",
    "prompt": "Is there cake at the end?",
    "max_tokens": 7,
    "temperature": 0
  }'
## response 
 {
  "id": "cmpl-99BG6yyVj8tASJaf33C8uSJpjyg9a",
  "object": "text_completion",
  "created": 1711975258,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": "\n\nThis is a test.",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 6,
    "completion_tokens": 6,
    "total_tokens": 12
  }
}
```

## GPT-3.5 Turbo fine-tunning and API updates
[OpenAI  fine-tunning docs](https://platform.openai.com/docs/guides/fine-tuning)

At a high level, fine-tuning involves the following steps:

1. Prepare and upload training data [training data](fine_tune\fine_tune.json)
2. Train a new fine-tuned model
3. Evaluate results and go back to step 1 if needed
4. Use your fine-tuned model

- Practical
  - Follow the steps to upload training data, fine-tune the model and test the model [Fine tune upload and training script](fine_tune\fine_tune.sh)

## Completion API 

### Used in Translation

- Its a zero-shot prompting and LLM relying on an LLM's existing understanding of the world to get an answer for a single prompt.
- General rule of thumb, the longer the response its less accurate.
- LLM respone may stop early or print more than the expected.
- It generally looks for stop words or stops at the max tokens specified.
- It will never print more the requested max tokens, eventhough the length is longer.
- The fewer words in the request, will be able to get response faster. This also decreases the cost of the query. The pay is based on the no of words in request, and response.

> Prompt: "Pleasse translate this article to $0 $1 in $2 words"  
- $0 language (Hindi)
- $1 article link or text
- $2 no of words in the response text
  
## Used in Summarization

> Prompt:
Please summarize this (article <article link> or text) in 100 words

## Google Gemini API

- [AI Google Dev](https://ai.google.dev/)



### Used in Chatbot

- Context is import. It uses the context in the previous chat conversation that provide guidance for the future output.

1. Build the context

```bash
System => You are a helpful assistant built to provide guidance on doing chores.
System => You're trained on white collar jobs like scheduling appointments, data entry, and making reservations.
User =>
· I need to make an appointment with Bob sagat tomorrow at 3pm Assistant =>
This is all one prompt, so the new response takes into account the previous messages to build the new response.
```

2. Translate to code

```json
{"role": "system", "content": "You are a helpful assistant built to provide guidance on doing chores."},
{"role": "system", "content": "You're trained on white collar jobs like scheduling appointments, data entry, and making reservations."},
{"role": "user", "content": " I need to make an appointment with Bob sagat tomorrow at 3pm Assistant "}
```

- Performance Considerations
  - Generally LLMs have a max context window size. If you hit the max context window size, you may need to increase the context window
  - You might need to break down complex prompts into smaller parts to get optimal performance.

## How to use image API

- [OpenAI Image Generation](https://platform.openai.com/docs/guides/images/usage?context=node)
  
- Parameters:

- Model - "dall-e-3" or "dall-e-2"
- Prompt - String
- Size-"1024x1024", "1024x1792", or
- "1792x1024"
- Quality - "standard" or "hd"
- N-Number of images at a time (1 for Dall-e 3 and 10 for Dall-e 2)
- Note: Dall-e 3 has built in safety features that will remove certain keywords (Hate, racism content).
- Editing, Image variation is only in Dall-e 2

## How to use the Text to Speech API

- Use this to
  
  - Narrate a blog post
  - Produce spoken audio in multiple language
  - Stream real time audio with the text to Speech API
