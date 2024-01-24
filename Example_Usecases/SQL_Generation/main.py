# main.py

import environment_setup
import dataset_preparation
import model_training
import model_evaluation

def main():
    # Set up the environment
    environment_setup.install_packages()

    # Prepare the NL2SQL dataset
    dataset = dataset_preparation.prepare_nl2sql_dataset()

    # Train the model
    trained_model_path = model_training.train_model(dataset)

    # Evaluate the model
    model_evaluation.evaluate_model(trained_model_path, dataset["validation"])

if __name__ == "__main__":
    main()
