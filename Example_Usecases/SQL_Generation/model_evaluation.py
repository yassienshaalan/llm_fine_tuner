from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from datasets import load_metric

def evaluate_model(model_path, eval_dataset):
    # Load the model and tokenizer
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    # Create the pipeline
    nlp = pipeline("text2sql", model=model, tokenizer=tokenizer)

    # Load the accuracy metric
    metric = load_metric("accuracy")

    results = []
    for example in eval_dataset:
        # Adjust these lines based on how your dataset is structured
        input_text = example["messages"][1]["content"]  # The user's question
        true_sql = example["messages"][2]["content"]  # The expected SQL response

        # Generate SQL using the model
        generated_sql = nlp(input_text)[0]["generated_text"]

        # Compare the generated SQL with the true SQL
        result = metric.compute(predictions=[generated_sql], references=[true_sql])
        results.append(result)

    # Calculate and print the average accuracy
    avg_accuracy = sum([r['accuracy'] for r in results]) / len(results)
    print(f"Average Accuracy: {avg_accuracy}")