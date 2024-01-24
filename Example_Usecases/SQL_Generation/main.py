import logging
import time
import environment_setup
import dataset_preparation
import model_training
import model_evaluation

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the environment setup...")
    start_time = time.time()
    environment_setup.install_packages()
    logging.info(f"Environment setup completed in {time.time() - start_time:.2f} seconds.")

    logging.info("Preparing the Spider dataset for NL2SQL task...")
    start_time = time.time()
    train_test_split = dataset_preparation.preprocess_spider_dataset()
    logging.info(f"Dataset preparation completed in {time.time() - start_time:.2f} seconds.")

    logging.info("Starting model training...")
    start_time = time.time()
    trained_model_path = model_training.train_model(train_test_split["train"])
    logging.info(f"Model training completed in {time.time() - start_time:.2f} seconds.")

    logging.info("Evaluating the model...")
    start_time = time.time()
    model_evaluation.evaluate_model(trained_model_path, train_test_split["validation"])
    logging.info(f"Model evaluation completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()