from datasets import load_dataset

# Download TinyStoriesInstruct
dataset = load_dataset("roneneldan/TinyStoriesInstruct", split="train")

# Save as text file (one story per line)
with open("tinystories.txt", "w", encoding="utf-8") as f:
    for item in dataset:
        # Extract just the story text
        story = item.get("story", "")
        if story:
            f.write(story.replace("\n", " ") + "\n")

print(f"Downloaded {len(dataset)} stories to tinystories.txt")