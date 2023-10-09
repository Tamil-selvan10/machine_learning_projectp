from collections import namedtuple

#1. Dataset Download URL
#2. Download Folder (Compressed File Folder)
#3. Extracted Folder (Extracted File Folder)
#4. Train Dataset Folder
#5. Test Dataset Folder
DataIngestionConfig=namedtuple(typename='DataIngestionConfig',
                               field_names=['dataset_download_url',
                                            'tgz_download_dir',
                                            'raw_data_dir',
                                            'ingested_train_dir',
                                            'ingested_test_dir'])

#1. Schema file path
DataValidationConfig=namedtuple(typename='DataValidationConfig',
                                field_names=['schema_file_path'])



DataTransformationConfig=namedtuple(typename='DataTransformationConfig',
                                    field_names=['add_bedroom_per_room',
                                                 'transformed_train_dir', # X_train_scaled
                                                 'transformed_test_dir',  # X_test_scaled
                                                 'preprocessed_object_file_path' # StandardScaler() - object
                                                 ])


ModelTrainerConfig=namedtuple(typename='ModelTrainerConfig',
                              field_names=['trained_model_file_path', # LinearRegression() - object
                                           'base_accuracy'
                                           ])

ModelEvaluationConfig=namedtuple(typename='ModelEvaluationConfig',
                                field_names=['model_evaluation_file_path','timestamp'])

ModelPusherConfig=namedtuple(typename='ModelPusherConfig',
                             field_names=['export_dir_path'])

TrainingPipelineConfig = namedtuple(typename="TrainingPipelineConfig", 
                                    field_names=["artifact_dir"])



