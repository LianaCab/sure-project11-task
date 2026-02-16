import json

def detect_ambiguity(structured_data, question):
    try:
        data = json.loads(structured_data)
    except:
        return {"full_response": structured_data}

    objects = data.get("objects", [])

    response = []
    ambiguous = False

    response.append("I detected the following objects:")

    for obj in objects:
        name = obj.get("name")
        count = obj.get("count", 1)
        location = obj.get("location", "unknown location")
        attributes = obj.get("attributes", "")

        if count > 1:
            ambiguous = True

        response.append(
            f"- {count} {name}(s) located {location}. {attributes}"
        )

    if ambiguous:
        response.insert(0, "There are multiple objects that may match your question.")

    return {
        "full_response": "\n".join(response)
    }
