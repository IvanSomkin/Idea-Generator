import random

producer_singular_set = ["company", "program", "business", "startup", "person"]
producer_action_infinitive_set = ["develop", "produce", "advance", "improve", "create", "generate", "find", "explore"]

product_adjective_set = ["random", "healthy", "interesting", "strong", "fast", "colorful", "environmentally-friendly", "3D", "2D", "racing", "adult", "violent"]
product_multiple_set = ["food", "gear", "clothing", "ideas", "sentences", "boxes", "bycicles", "cars", "trains", "paintings", "social networks", "mobiles apps", "plugins", "programms", "applications", "video games"]

client_adjective_set = ["young", "old", "fit", "overweight", "fitness", "mountain", "clean", "Russian", "English", "American", "French", "German", "Spanish", "Polish", "Hungarian", "Chinese", "Japanese"]
client_multiple_set = ["people", "dogs", "cats", "birds", "monkeys", "elephants", "businesses", "companies", "teachers", "students", "gyms", "programmers", "web-developers", "game-developers", "casinos"]

producer = random.choice(producer_singular_set)
producer_action = random.choice(producer_action_infinitive_set)
product = random.choice(product_multiple_set)
product_adjective = random.choice(product_adjective_set)
client = random.choice(client_multiple_set)
client_adjective = random.choice(client_adjective_set)


sentence = "A "
sentence += producer
sentence += " that "
sentence += producer_action + "s"
sentence += " "
sentence += product_adjective
sentence += " "
sentence += product
sentence += " for "
sentence += client_adjective
sentence += " "
sentence += client


print(sentence)