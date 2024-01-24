import environment_setup
import dataset_preparation
import model_training
import model_evaluation
import model_deployment

def main():
    # Step 1: Setup the environment
    environment_setup.install_packages()

    # Step 2: Prepare the dataset
    dataset = dataset_preparation.prepare_dataset()

    # Step 3: Train the model
    trained_model_path = model_training.train_model(dataset)

    # Step 4: Evaluate the model
    eval_results = model_evaluation.evaluate_model(trained_model_path, dataset["test"])

    # Print evaluation results
    print(f"Model Evaluation Results: {eval_results}")

    # Step 5 (Optional): Deploy the model
    # Uncomment the following line if deployment is needed
    # model_deployment.deploy_model(trained_model_path)

if __name__ == "__main__":
    main()
