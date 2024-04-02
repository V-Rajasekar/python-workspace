from openai import OpenAI

client = OpenAI()

MODEL = ["dall-e-3", "dall-e-2"]

RESOLUTION = ["1024x1024", "1024x1792", "1792x1024"]

QUALITY = ["standard", "hd"]

PROMPTS = [
    "Futuristic Los Angeles, highly detailed, Dystopian City Building, photographic, Volumetric Lighting, Rain Storm, Future Vehicles, designed by Syd Mead, professional ominous concept art, by artgerm and greg rutkowski, an intricate, elegant, highly detailed digital painting, concept art, smooth, sharp focus, illustration, in the style of simon stalenhag, wayne barlowe, and igor kieryluk,",
    "High-resolution Architecture Photography in a 4:3 ratio: An intricately detailed image capturing a contemporary building that appears to be suspended above the clouds. The edifice is artistically constructed from pink plush material interspersed with white feathers. A notable feature is a large flamingo head emerging from the building, adding a surreal touch to the scene. This imaginative building contrasts beautifully against a serene sky backdrop, and the image's quality hints at being captured with a Canon RF 28-70mm f/2L USM lens. Every texture, from the plush to the feathers to the flamingo's details, is rendered with impeccable clarity, creating a surreal yet aesthetically striking visual.",
    "creat this image become indochine house picture",
    "lien ruins, scifi, future, golden ratio, by Edmund Blair Leighton, Brom, Charlie Bowater, faces by Tom Bagshaw, Sargent, Award - winning, photograph shot with Kodak Portra 800, a Hasselblad 500C, 55mm f/ 1. 8 lens, extreme depth of field, available light, high contrast, Ultra HD, HDR, DTM, 8K",
    "Ultra-detailed Architecture Photography in a 4:3 ratio: A mesmerizing image showcasing a modern building submerged under the sea. The structure, with its sleek lines and contemporary design, stands in stark contrast to the aquatic surroundings. Marine life, from colorful fish to swaying seaweed, dances around the building, while beams of sunlight pierce through the water's surface, casting a magical glow. The photograph's quality hints that it was captured using a Canon RF 28-70mm f/2L USM lens. Every detail, from the architectural features of the building to the textures of the marine environment, is rendered with impeccable clarity, resulting in a surreal yet profoundly aesthetic composition."
]


def generate_image_with_prompt(prompt: str, model: str, resolution: str = "1792x1024", quality: str = "standard", quantity: int = 1):
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=resolution,
        quality=quality,
        n=quantity,
    )

    urls = []
    for data in response.data:
        urls.append(data.url)
    return urls


print()
print()
print("Generating images...")
print()
print()
for url in generate_image_with_prompt(
        PROMPTS[1], MODEL[1], RESOLUTION[0], QUALITY[0], 4):
    print(f"url: {url}")
print()
print()
