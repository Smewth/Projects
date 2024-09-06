from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-2",
  prompt="I want you to give me an image based off of the Knight in Dark Souls, but on his back, in bit-art",
  size='1024x1024',
  quality="standard",
  n=1,
)

image_url = response.data[0].url