import time
import random
import json
import os 
from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData

# --- CONFIGURATION ---
# Paste the long string starting with "Endpoint=sb://..." here
load_dotenv()  #This line wakes uop the .env file and loads the variables into the environment


CONNECTION_STRING = os.getenv("CONNECTION_STRING ")  # Fetch the connection string from environment variables

# --- SIMULATION DATA ---
LOCATIONS = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Pune']
MERCHANTS = ['Starbucks', 'Uber', 'Amazon', 'Croma', 'Tanishq']
CARD_TYPES = ['Visa', 'MasterCard', 'Rupay']



def generate_transaction():
    """Generates a fake transaction."""
    is_fraud = random.random() < 0.05
    txn = {
        "transaction_id": f"TXN-{random.randint(1000000, 9999999)}",
        "timestamp": str(time.time()),
        "amount": round(random.uniform(50000, 200000) if is_fraud else random.uniform(10, 5000), 2),
        "merchant": random.choice(MERCHANTS),
        "location": random.choice(LOCATIONS),
        "card_type": random.choice(CARD_TYPES),
        "is_fraud_flag": is_fraud
    }
    return txn

def send_data():
    # Create the client
    client = EventHubProducerClient.from_connection_string(CONNECTION_STRING)
    
    with client:
        print("🚀 Connected to Fabric! Sending data...")
        while True:
            # Create a batch of data
            event_data_batch = client.create_batch()
            
            # Generate a transaction
            txn = generate_transaction()
            json_txn = json.dumps(txn)
            
            # Add to batch
            event_data_batch.add(EventData(json_txn))
            
            # Send the batch
            client.send_batch(event_data_batch)
            
            status = "🔴 FRAUD" if txn['is_fraud_flag'] else "🟢 Normal"
            print(f"[{status}] Sent ₹{txn['amount']} at {txn['location']}")
            
            time.sleep(1) # Wait 1 second

if __name__ == "__main__":
    send_data()