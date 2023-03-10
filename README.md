# DSC-180B-Project
GROUP NAME: AC/DS :metal: (Angela + Cecilia -> AC, Data Science -> DS, AC/DC -> AC/DS) :fist_right::fist_left:
- classification of penumothorax dataset CANDID-PTX

**Brave Angela Not Afraid of Error :partying_face:**

**Be Calm and Write Code Cecilia :innocent:**

## Goal :pray:
- [x] Birthday (Angela) :birthday:
- [x] Classification Final Results
- [x] Segmentation Final Results
- [ ] Cascade Final Results
- [ ] Poster [03/09 DDL]
- [ ] Website/Report/Code [03/14 DDL]
- [ ] Presentation/Birthday (Cecilia) :birthday: [03/15 DDL]

### Current ensemble approach
1. Binarized mask
- binarized mask as input for classification model
- extended gray-scale mask (max-value convolutional kernel to extend the mask area to include the "sharp edge")
2. Probability mask
- prabability mask as input for classfication model
- 2-channel mask with original xray value + probability mask

## Website
If you just want to have an idea of what this project is about without seeing all these codes (which I understand :stuck_out_tongue_winking_eye:), click here :point_right: https://angela-wang111.github.io/Pneumothorax_classification/

## Documentation
The useful files for checkpoint testing phase are: run.py, submission.json, src(folder), test(folder), and outpout(folder). 

:heavy_exclamation_mark:Execution instruction (in terminal):
1. `ssh <username>@dsmlp-login.ucsd.edu`
2. `launch.sh -i angela010101/quarter1:latest -c 8 -m 64 -g 1` at least 1 GPU and 64 GB memory is needed
3. `git clone https://github.com/Angela-Wang111/Pneumothorax_classification` (first time execution only)
4. `cd Pneumothorax_classification`
5. `python run.py`
6. :crossed_fingers:
### submission.json
Contains the URLs for this Github Repository and the DockerHub Repository used for building a docker image for this pipeline.
### run.py
This is the main .py file for executing the whole pipeline from data preprocessing to training and test both classification model (ResNet 34) and segmentation model (ResNet 34 + U-Net). To run it, just run `python run.py` in the terminal (and hope everything goes fine :crossed_fingers: ).
### src
#### data_preprocessing.py
This file contains functions to decode the RLE encoded pixels from the source "test/testdata/Pneumothorax_reports_small.csv" file and to save both positive and negative masks into test/testdata/masks, so they could be used for the segmentation model training/testing.
#### generate_train_val_test_csv.py
This file contains functions to generate "test/testdata/train.csv", "test/testdata/validation.csv", and "test/testdata/test.csv" for model training/validation/test.
#### create_dataloader.py
This file contains functions to create dataframe from .csv file like "test/testdata/train.csv", create custermized Dataset, and create DataLoader. The function to create customized Dataset is modified to read .png formatted original images. The full version code is written to read DICOM format images stored in the team group folder.
#### build_classification_model.py
This file contains functions to build customized pretrained ResNet 34 model and train/validate ResNet 34 model.
#### evaluate_test.py
*evaluate_test_empty.py* for now. Wait for later implementation.
This file contains fucntions to perform the classification on the test set, and evaluate the predication with metrics like confusion matrix and AUC-ROC score.

### test
All the data here are just a small portion of CANDID-PTX (100/19237) for pipeline testing purpose only since the original data size is ~30GB.
#### testdata
- *Pneumothorax_reports_small.csv*: source test .csv file. Includes 100 penumothorax samples (15 positive, 85 negative) with **SOPInstanceUID** to identify each sample, and **EncodedPixels** to specify the penumothorax region (in RLE encoded format if positive, -1 if negative).
- *images*: folder contains the original X-Ray images (1024x1024). Named in the format "\<SOPInstanceUID>.png". The original images are in DICOM format, but are changed to .png format for the pipeline testing purpose. 
- *masks*: empty folder to store the decoded binary masks.

After runing the pipeline, the following files would be created :point_down:
- *masks*: folder contains the decoded binary masks (1024x1024). Named in the format "\<SOPInstanceUID>.png" if positive, "negative_mask.png" if negative.
- *train.csv*: training set with 80 samples (12 postive, 68 negative).
- *validation.csv*: validation set with 10 samples (2 positive, 8 negative).
- *test.csv*: test set with 10 samples (1 positive, 9 negative).

### output
This should be an empty folder before executing the pipeline. After executing the pipeline, the following files would be created :point_down:
- *train_val_loss_ResNet34.png*: the train and validation loss for each epoch during model training process.
