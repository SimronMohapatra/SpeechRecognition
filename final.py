import speech_recognition as sr
import boto3
import sys
# obtain path to "brian.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "brian.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


client_comprehend = boto3.client(
    'comprehend',
    region_name='eu-west-1',
    aws_access_key_id='AKIAJ3SKR3SWDGLZGLTQ',
    aws_secret_access_key='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'
)


def process_document(file_path):
    filename = file_path.split("/")[-1]
    extension = filename.split(".")[-1]

    plain_text = r.recognize_sphinx(audio)
    # you can find the methods to extract the text from different document here:
    # https://gist.github.com/mz1991/97ee3f7045c8fd0e6f21ab14f9e588c7
    if extension == "pdf":
        plain_text = get_pdf_text(file_path)
    if extension == "docx":
        plain_text = get_docx_text(file_path)
    if extension == "txt" or extension == "csv":
        plain_text = get_txt_text(file_path)
        # Add your custom file extension handler


    # Max Bytes size supported by AWS Comprehend
    # https://boto3.readthedocs.io/en/latest/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language
    # https://boto3.readthedocs.io/en/latest/reference/services/comprehend.html#Comprehend.Client.detect_entities
    while sys.getsizeof(plain_text) & gt:
        plain_text = plain_text[:-1]

    dominant_language_response = client_comprehend.detect_dominant_language(
            Text=plain_text
        )
    dominant_language = sorted(dominant_language_response['Languages'], key=lambda k: k['LanguageCode'])[0][
            'LanguageCode']

        # The service now only supports English and Spanish. In future more languages will be available.
    if dominant_language not in ['en', 'es']:
        dominant_language = 'en'

    response = client_comprehend.detect_entities(Text=plain_text,LanguageCode=dominant_language)
    entites = list(set([x['Type'] for x in response['Entities']]))

    return entites

    response_key_phrases = client_comprehend.detect_key_phrases(Text=plain_text,LanguageCode=dominant_language)
    key_phrases = list(set([x['Text'] for x in response_key_phrases['KeyPhrases']]))

    return key_phrases


    response_sentiment = client_comprehend.detect_sentiment(Text=plain_text,LanguageCode=dominant_language)
    sentiment = response_sentiment['Sentiment']
    response_sentiment = client_comprehend.detect_sentiment(
    Text=plain_text,
    LanguageCode=dominant_language
    )
    sentiment = response_sentiment['Sentiment']
    return sentiment