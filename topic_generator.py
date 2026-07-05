from transformers import pipeline
from transformers import set_seed

generator = pipeline(
    "text-generation",
    model="gpt2"
)

set_seed(42)


def generate_topics(themes, interests):

    prompt = f"""
I am attending an event about {', '.join(themes)}.
My interests are {', '.join(interests)}.

Generate 3 professional networking conversation starters:
"""

    result = generator(
        prompt,
        max_length=100,
        num_return_sequences=1
    )

    text = result[0]["generated_text"]

    lines = text.split("\n")

    suggestions = []

    for line in lines:
        line = line.strip()

        if len(line) > 20:
            suggestions.append(line)

    return suggestions[:3]


print(
    generate_topics(
        ["Artificial Intelligence", "Cloud Computing"],
        ["AI", "Machine Learning"]
    )
)