from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as C1Image
from selenium import webdriver

def website_snapshot(url):
    """Takes a snapshot of the URL provided, saving it to the snapshots
    folder along with returning a path to the file.

    :param url: String of the URL to capture
    :return: String of the image file path
    """

    driver = webdriver.PhantomJS()
    #driver.set_window_size(1024, 768) # set the window size, but cuts out
    driver.get(url)

    # Encode the image
    #image_64_encode = base64.encodestring()

    clean_url = url.replace('https://', '').replace('/', '_').replace('-', '_').replace('.', '_')
    save_path = 'snapshots/' + clean_url + '.png'

    driver.save_screenshot(save_path)
    driver.quit
    return save_path


def clarifai_analysis(img_path, keys, n=3, url_source=True):
    """Send an image to clarifai to have its features classified, returning
    the top n concepts as a list (based on accuracy).

    :param img_path: String of the file path to the image
    :param keys: Dictionary of API keys
    :param n: Integer of how many of the top concepts should be returned
    :param url_source: Boolean of where the img_path is from; a url or a file
        path. If the img_path is from a url, provide True
    :return: List of the top concepts from the image
    """

    # Initialize the clarifai api
    app = ClarifaiApp(keys['clarifai_id'], keys['clarifai_secret'])
    
    # Get the general model
    model = app.models.get('general-v1.3')

    if url_source:
        # Send a url link of the image to the model
        image = C1Image(url=img_path)
    else:
        # Send a image from the file path to the model
        image = C1Image(file_obj=open(img_path, 'rb'))

    try:
        # Send the image to clairifai api to be proceessed
        classification_data = model.predict([image])
    except Exception as e:
        # Return a list with 3 empty strings if the prediction fails
        print('WARNING! Clairifai was unable to process the article image.')
        return ['', '', '']
    
    # Pull out the concepts from the classification analysis
    concepts = classification_data['outputs'][0]['data']['concepts']
    top_concepts = []
    for i in range(n):
        top_concepts.append(concepts[i]['name'])

    return top_concepts


if __name__ == '__main__':

    from key_store import key_store
    test_keys = key_store()

    test_url = 'https://github.com'
    test_img_save_path = website_snapshot(test_url)

    test_top_concepts = clarifai_analysis(test_img_save_path, test_keys,
                                          url_source=False)
    print(test_top_concepts)

    test_url_image = 'https://static5.businessinsider.com/image/555f4a026bb3f7102072d40a/elon-musk-didnt-like-his-kids-school-so-he-made-his-own-small-secretive-school-without-grade-levels.jpg'
    test_url_top_concepts = clarifai_analysis(img_path=test_url_image,
            keys=test_keys)
    print(test_url_top_concepts)
