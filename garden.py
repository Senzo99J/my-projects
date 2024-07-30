import spacy
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# List of garden path sentences
gardenpathSentences = ["The old man and boats", "Mary gave the child a Band-Aid", "The cotton clothing is made of grows in Mississippi-"]

# Process each sentece
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"\nSentence:{sentence}")

    # Tokenization and Named Entity Recognition
    print("Entities:")
    for entity in doc.ents:
        print(f"-{entity.text},({entity.label_}):{spacy.explain(entity.label)}")

        # Explanation of entities
        for entity in doc.ents:
            print(f"\nEntity:{entity.text}")
            print(f"Explonation:{spacy.explain(entity.label_)}")
            print(f"Does the entity make sense:{spacy.explain(entity.label_)}")

# Write about two entities
with open("output.txt", "w") as f:
    f.write("Two entities explained:\n")
    for i, entity in enumerate(doc.ents[:2]):
        f.write(f"Entity {i+1}: {entity.text}\n")

        f.write(f"Explanation:{spacy.explain(entity.label_)}")

        f.write(f"Does the entity make sense:{entity.text} is a {spacy.explain(entity.label_)}\n")

        f.write("\n")