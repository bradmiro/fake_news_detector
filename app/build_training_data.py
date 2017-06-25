import csv
import os
import pandas as pd

from main import main


def build_training_data():

    # Open the facebook fact check sheet into a pandas dataframe
    dir = os.path.dirname(__file__)
    data_file = os.path.join(dir, 'data', 'formatted_kaggle_training_data.csv')
    source_df = pd.read_csv(data_file)

    # Save the training data to a CSV for later processing
    out_csv = os.path.join(dir, 'data', 'training_data.csv')
    if os.path.isfile(out_csv):
        raise SystemError('The training_data.csv file already exists. Change '
                          'the file name before running this code to prevent '
                          'it from being overwritten.')

    # Create output CSV file with header rows
    with open(out_csv, 'w') as training_data_csv:
        writer = csv.writer(training_data_csv)
        writer.writerow(['source', 'author', 'date', 'text', 'title',
                         'image_tag_1', 'image_tag_2', 'image_tag_3',
                         'spelling', 'sentiment'])
    
    # Iterate through all articles
    for index, row in source_df.iterrows():
        article_parameters = {'source': row['site_url'],
                              'author': row['author'],
                              'date': row['published'],
                              'text': row['text'],
                              'title': row['title'],
                              'image': row['main_img_url'],
                              }

        # Add final parameeters to CSV
        final_parameters = main(article_parameters=article_parameters)
        important_params = [final_parameters['source'],
                            final_parameters['author'],
                            final_parameters['date'],
                            final_parameters['text'],
                            final_parameters['title'],
                            final_parameters['image_tag_1'],
                            final_parameters['image_tag_2'],
                            final_parameters['image_tag_3'],
                            final_parameters['spelling'],
                            final_parameters['sentiment']]
        with open(out_csv, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(important_params)
        

if __name__ == '__main__':

    build_training_data()
