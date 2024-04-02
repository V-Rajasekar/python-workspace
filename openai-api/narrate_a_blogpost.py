from pathlib import Path
from openai import OpenAI

client = OpenAI()

MODEL = ["tts-1", "tts-1-hd"]

VOICE = [
    "alloy",
    "echo",
    "fable",
    "onyx",
    "nova",
    "shimmer"
]

BLOG_TEXT = """
In a rapidly evolving digital landscape, artificial intelligence (AI) has become an indispensable tool in our daily lives. OpenAI's GPT models and the recent introduction of GPTs for fine-tuning have marked a significant milestone in AI development. These advancements have not only provided a general framework for AI capabilities but have also empowered users to tailor AI systems to suit their specific needs. This article explores how LLMs have paved the way for the golden era of fine-tuning, enabling users to create their own AI assistants.

The Power of GPT Assistants:
In an era where information overload is a constant challenge, GPT assistants have emerged as valuable tools for enhancing productivity and simplifying workflows. According to a Zapier's blog post, GPT assistants can help users with a wide variety of tasks, ranging from generating code snippets to drafting emails. By harnessing the power of GPT models, users can now delegate monotonous and time-consuming tasks to AI systems, freeing up valuable time for more creative and strategic endeavors, however GPTs are inherently more general.

Building off of the base:
Up to now, GPTs have been too general to be used effectively in most industries. The introduction of GPTs for fine-tuning, as reported by The Verge, has revolutionized the AI landscape. OpenAI's GPT models act as a starting point, providing a solid foundation for users to customize and train their own AI systems. This customized approach allows users to impart specific knowledge and biases to the AI models, making them more aligned with their unique requirements. Whether it's a legal assistant well-versed in specific jurisdictions or a medical AI capable of diagnosing rare conditions, the possibilities for customization are endless.
"""


def convert_body_to_speech(input_text: str, voice: str, hd: bool, output_path: str):
    response = client.audio.speech.create(
        model=MODEL[0] if hd else MODEL[1],
        voice=voice,
        input=input_text,
    )

    response.stream_to_file(output_path)


speech_file_path = Path(__file__).parent / "fable.mp3"

print()
print("Transcoding text...")
convert_body_to_speech(BLOG_TEXT, VOICE[2], False, speech_file_path)
print("Done!")
print()
print(f'Output path: {speech_file_path}')
