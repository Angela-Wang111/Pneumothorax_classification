import sys
import os
import json

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib.cm as cm
import os

sys.path.insert(0, 'src')

# Import functions from other py files
from data_preprocessing import save_positive_masks
from data_preprocessing import save_negative_masks
from data_preprocessing import decode_mask

from generate_train_val_test_csv import generate_three_csv

from create_dataloader import create_loader

from build_classification_model import resnet34
from build_classification_model import training_classifier

# Hyperparameters for dataloader
RESOLUTION = 256
BATCH_SIZE = 4
NUM_WORKERS = 4
PIN_MEMORY = True
DROP_LAST = True

# Hyperparameters for model training
NUM_EPOCHS = 5
LEARNING_RATE = 1e-4
THRESHOLD = 0.3


def main():
    """
    Run the main project pipeline logic
    """
    # Data Preprocessing
    decode_mask("test/testdata/Pneumothorax_reports_small.csv", "test/testdata/masks/")
    generate_three_csv("test/testdata/Pneumothorax_reports_small.csv")
    # Generate Data Loader for classification models
    train_loader_c, val_loader_c, test_loader_c = create_loader(RESOLUTION, 'C', BATCH_SIZE, NUM_WORKERS,             PIN_MEMORY, DROP_LAST)
    model = resnet34()
    model_c, all_train_loss_c, all_val_loss_c = training_classifier(model, NUM_EPOCHS, BATCH_SIZE, LEARNING_RATE,     train_loader_c, val_loader_c, RESOLUTION)
    
    
    
    
if __name__ == '__main__':
#     targets = sys.argv[1:]
    main()