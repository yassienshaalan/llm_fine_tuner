# model_training.py

from transformers import AutoModelForSeq2SeqLM, TrainingArguments, Trainer
from dataset_preparation import prepare_nl2sql_dataset

def train_model():
    model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")  # or another suitable model

    training_args = TrainingArguments(
        output_dir="./model_output",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        logging_dir='./logs',
        logging_steps=10,
        evaluation_strategy="epoch"
    )

    dataset = prepare_nl2sql_dataset()

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"]
    )

    trainer.train()

if __name__ == "__main__":
    train_model()
