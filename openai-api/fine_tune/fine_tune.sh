export OPENAI_API_KEY={Replace with your API Secret Key}
export FINE_TUNE_FILE=D:\\Git\\python-workspace\\openai-text\\fine_tune\\fine_tune.json


# Upload the file to OpenAI Servers
curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "purpose=fine-tune" \
  -F "file=@$FINE_TUNE_FILE" 

# Copy id from returned response 
# Start the fine tuning job
curl https://api.openai.com/v1/fine_tuning/jobs \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "training_file": "<Replace with your file id>",
  "model": "gpt-3.5-turbo-0613"
}'

## Copy fine tuning job "id": "ftjob-JnRvu1fXB6K3HkKCjO2xUY5b" from response
# Get the fine tuning jobs list
curl https://api.openai.com/v1/fine_tuning/jobs \
  -H "Authorization: Bearer $OPENAI_API_KEY"


# Get all of the events for the fine tuning job look for succeeded event copy  "fine_tuned_model": "ft:gpt-3.5-turbo-0613:personal::99PeogXb",
curl https://api.openai.com/v1/fine_tuning/jobs/{ft_job_id}/events \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Test the fine tuned model
curl https://api.openai.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "model": "<Replace with your model id>",
  "messages": [
    {
      "role": "system",
      "content": "You are an assistant that occasionally misspells words"
    },
    {
      "role": "user",
      "content": "Hello! What is fine-tuning?"
    }
  ]
}'