from datasets import load_dataset

def create_conversational_format(sample):
    """
    Converts dataset samples to a conversational format.
    """
    system_message = "You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA.\nSCHEMA:\n"
    return {
        "messages": [
            {"role": "system", "content": system_message + sample["db_id"]},
            {"role": "user", "content": sample["question"]},
            {"role": "assistant", "content": sample["query"]}
        ]
    }

def preprocess_spider_dataset():
    # Load the Spider dataset
    print("Load the Spider dataset")
    dataset = load_dataset("spider")
    print("dataset",type(dataset),dataset)
    
    # Using map to apply the conversational format conversion
    dataset = dataset.map(create_conversational_format, 
                          remove_columns=['db_id', 'query', 'question', 'query_toks', 'query_toks_no_value', 'question_toks']) # Remove the original columns if they are no longer needed

    print("dataset after",type(dataset),dataset)
    # Split the dataset into training and testing (customize split as needed)
    train_test_split = dataset["train"].train_test_split(test_size=0.1)
    return train_test_split

if __name__ == "__main__":
    processed_dataset = preprocess_spider_dataset()
    # Example: Save to disk or further processing
    processed_dataset["train"].to_json("train_dataset.json", orient="records")
    processed_dataset["test"].to_json("test_dataset.json", orient="records")
