# imports
import streamlit as st
import time
from openai import OpenAI


# statics
st.header('Story Generator')
def story_ai(msg, client):
  story_response = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[{
          'role':
          'system',
          'content':
          'You are bestseller story writer. You will take user'
          's pormpt and generate a 100 words short story for adults age 20-30'
      }, {
          'role': 'user',
          'content': f'{msg}'
      }],
      max_tokens=400,
      temperature=0.8)

  story = story_response.choices[0].message.content
  return story


def design_ai(story, client):
  design_response = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[{
          "role":
          'system',
          "content":
          '''Based on the story given, you will design a detailed image prompt for the cover image of this story. 
        The image prompt should include the theme of the story with relevant color, suitable for adults.
        The output should be within 100 characters.
        '''
      }, {
          "role": "user",
          "content": f'{story}'
      }],
      max_tokens=100,
      temperature=0.8)

  design = design_response.choices[0].message.content
  return design


def image_ai(design_prompt, client):
  cover_response = client.images.generate(model='dall-e-2',
                                          prompt=f'{design_prompt}',
                                          size='256x256',
                                          quality='standard',
                                          n=1)

  image_url = cover_response.data[0].url
  return image_url

from pathlib import Path

# def audio_ai(story_prompt, client):
#   speech_file_path = Path(__file__).parent / "speech.mp3"
#   audio = client.audio.speech.create(
#     model="tts-1",
#     voice="alloy",
#     input=f'{story_prompt}'
#   )
  
#   return audio

# methods
api_key = st.secrets["OPENAI_SECRET"]
client = OpenAI(api_key=api_key)

with st.form('This is a form'):
  st.write('This is for user to key in information')
  msg = st.text_input(label='Some keywords to generate a story')
  submitted = st.form_submit_button('Submit')
  
  if submitted:
    with st.spinner('Wait for the story generate...'):
      story = story_ai(msg, client)
      refined_prompt = design_ai(story, client)
      st.write(story)
      st.toast('Story generated done!')
      # st.success('Story generated done!')
    with st.spinner('Wait for the image generate...'):
      image_url = image_ai(refined_prompt, client)
      st.image(image_url)
      st.toast('Image generated done!')
    # with st.spinner('Wait for the audio generate...'):
    #   audio_ai(story, client)
    #   st.audio("speech.mp3", format="audio/mpeg", loop=True)
    #   st.toast('Audio generated done!')
  
  

# if st.button("Generate"):
#   story = story_ai(msg, client)
#   st.write(story)
