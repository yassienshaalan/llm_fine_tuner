from transformers import AutoModelForSeq2SeqLM, TrainingArguments, Trainer

def train_model(train_dataset):
    # Load the model, T5 or any other suitable Seq2Seq model
    model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./model_output",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        logging_dir='./logs',
        logging_steps=10,
        evaluation_strategy="epoch"
    )

    # Initialize the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        # If you have a separate validation dataset, load it here
        # eval_dataset=validation_dataset
    )

    # Start training
    trainer.train()

    # Save the trained model
    model.save_pretrained("./model_output")

    # Return path to the saved model
    return "./model_output"


