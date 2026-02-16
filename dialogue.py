import json

class DialogueManager:
    def __init__(self):
        self.context = None

    def handle_turn(self, structured_data, question):
        try:
            data = json.loads(structured_data)
        except:
            return structured_data

        objects = data.get("objects", [])

        if not self.context:
            self.context = objects
            names = [obj["name"] for obj in objects]
            return (
                f"I see the following objects: {', '.join(names)}. "
                "Which one would you like more details about?"
            )

        else:
            for obj in self.context:
                if obj["name"].lower() in question.lower():
                    return (
                        f"{obj['count']} {obj['name']}(s), "
                        f"located {obj.get('location')}. "
                        f"{obj.get('attributes')}"
                    )

            return "Please specify which object you are referring to."
