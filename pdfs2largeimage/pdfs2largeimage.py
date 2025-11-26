from __future__ import annotations
import pathlib
from PIL import Image
import pdf2image

def pdf_to_images(*pdf_paths: list[str], dpi: int = 200) -> list[Image.Image]:
    images: list[Image.Image] = list[Image.Image]()
    for pdf_path in pdf_paths:
        images.append(pdf2image.convert_from_path(pdf_path=pdf_path, dpi=dpi, first_page=1, last_page=1)[0])
    return images

def images_to_large_image(row: int, column: int, *images: list[Image.Image]) -> Image.Image:
    if len(images) != row * column:
        raise ValueError('The number of images does not match the specified grid size.')
    width: int = max(image.width for image in images)
    height: int = max(image.height for image in images)
    large_image: Image.Image = Image.new('RGB', (width * column, height * row), (255, 255, 255))
    for index, image in enumerate(images):
        x: int = (index % column) * width + (width - image.width) // 2
        y: int = (index // column) * height + (height - image.height) // 2
        large_image.paste(image, (x, y))
    return large_image

def pdfs_to_large_image(row: int, column: int, *pdf_paths: list[str], dpi: int = 200, save_pdf_path: str | None = None) -> Image.Image:
    images: list[Image.Image] = pdf_to_images(*pdf_paths, dpi=dpi)
    large_image: Image.Image = images_to_large_image(row, column, *images)
    if save_pdf_path is not None:
        save_dir: pathlib.Path = pathlib.Path(save_pdf_path).parent
        save_dir.mkdir(parents=True, exist_ok=True)
        large_image.save(save_pdf_path, 'PDF')
    return large_image