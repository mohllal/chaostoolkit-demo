#!/bin/bash

# Create directories for journals and logs if they don't exist
mkdir -p ./experiments/journals
mkdir -p ./experiments/logs

# Loop through all experiment files in the experiments directory
for experiment_file in ./experiments/*.json; do
  if [ -f "$experiment_file" ]; then
    # Extract experiment name without extension
    experiment_name=$(basename "$experiment_file" .json)
    echo "Running experiment: $experiment_name"
    
    # Define output paths
    journal_path="./experiments/journals/${experiment_name}-journal.json"
    log_file="./experiments/logs/${experiment_name}-log.txt"
    
    # Run the experiment and save journal
    chaos --log-file "$log_file" run "$experiment_file" --journal-path "$journal_path"
    
    echo "Completed experiment: $experiment_name"
    echo "-------------------------------------------"
  fi
done

echo "All experiments completed"
