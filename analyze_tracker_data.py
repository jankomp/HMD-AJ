import csv
from pymongo import MongoClient

# Create a client to connect to your MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Connect to your 'rasa' database
db = client['rasa']

# Access the 'conversations' collection
conversations = db['conversations']

# Fetch all documents in the 'conversations' collection
all_conversations = conversations.find()

# Open a CSV file to write the data
with open('conversations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Conversation ID", "Event", "Policy", "Timestamp", "Intent", "Text", "Metadata", "Latest Event Time", "Name", "Value"])

    # Iterate over the conversations
    for conversation in all_conversations:
        # Iterate over the events in each conversation
        for event in conversation['events']:
            # Write a row for each event
            writer.writerow([
                conversation['_id'],
                event['event'],
                event.get('policy', ''),  # Some events might not have a 'policy' field
                event['timestamp'],
                event.get('parse_data', {}).get('intent', {}).get('name', ''),  # Some events might not have a 'parse_data' field
                event.get('text', ''),  # Some events might not have a 'text' field
                event.get('metadata', ''),  # Some events might not have a 'metadata' field
                conversation['latest_event_time'],
                event.get('name', ''),  # Some events might not have a 'name' field
                event.get('value', ''),  # Some events might not have a 'value' field
            ])