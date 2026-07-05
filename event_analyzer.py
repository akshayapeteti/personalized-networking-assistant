from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

def extract_event_themes(description):

    labels = [
        "Artificial Intelligence",
        "Machine Learning",
        "Cloud Computing",
        "Cybersecurity",
        "Blockchain",
        "Healthcare",
        "Education",
        "Business",
        "Networking"
    ]

    result = classifier(
        description,
        labels
    )

    return result["labels"][:3]


print(
    extract_event_themes(
        "A conference about AI and Cloud Computing"
    )
)