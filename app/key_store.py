def key_store():
    """Store API keys in a dictionary.

    DO NOT COMMIT KEYS 

    :return: Dictionary of API keys
    """

    bing_spell_check = ''
    language_understanding = ''
    text_analytics = ''
    linguistic_analysis = ''
    bing_image_search = ''
    bing_video_search = ''
    
    key_dict = {
        'bing_spell_check': bing_spell_check,
        'language_understanding': language_understanding,
        'text_analytics': text_analytics,
        'linguistic_analysis': linguistic_analysis,
        'bing_image_search': bing_image_search,
        'bing_video_search': bing_video_search,
    }
    return key_dict
