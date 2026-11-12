c = [
    {
        "role": "user",
        "parts": [
            {"text": "What is AI?",
             "viv":1},
             {
                 "s":"s"
             }
        ]
    },
    {
        "role": "model",
        "parts": [
            {"text": "AI is Artificial Intelligence."}
        ]
    }
]
print(c[0]['parts'][1]['s'])