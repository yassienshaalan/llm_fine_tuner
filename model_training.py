# model_training.py

from transformers import AutoModelForCausalLM, TrainingArguments, Trainer
from your_dataset_module import load_and_prepare_dataset

def train_model():
    model = AutoModelForCausalLM.from_pretrained("your-model-name")
    
    training_args = TrainingArguments(
        output_dir="./model_output",
        num_train_epochs=3,
        per_device_train_batch_size=16,
        logging_dir='./logs',
        logging_steps=10,
    )

    dataset = load_and_prepare_dataset()
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"]
    )

    trainer.train()

if __name__ == "__main__":
    train_model()
