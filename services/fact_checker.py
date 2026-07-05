import wikipedia


def fact_check(topic):
    try:
        return wikipedia.summary(
            topic,
            sentences=2
        )
    except:
        return "No information found."