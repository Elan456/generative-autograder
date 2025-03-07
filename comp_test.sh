curl -X POST "http://localhost:8081/v1/chat/completions" \
     -H "Content-Type: application/json" \
     -d '{
           "messages": [
             {"role": "system", "content": "You are a helpful assistant."},
             {"role": "user", "content": "Tell me about NVIDIA RAG Server."}
           ],
           "use_knowledge_base": true,
           "temperature": 0.2,
           "top_p": 0.7,
           "max_tokens": 1024,
           "top_k": 4,
           "collection_name": "nvidia_blogs",
           "model": "meta/llama-3.1-70b-instruct",
           "stop": []
         }'
