"""Generate thumbnail versions of all gallery images."""

from pathlib import Path
from PIL import Image, ImageOps

ASSETS_DIR = Path(__file__).parent / "assets"
MAX_SIZE = 600
QUALITY = 80

ASSET_DIRS = [
    "1. Small Format Works",
    "2. Medium Format Works",
    "3. Large Format Works",
    "4. Photo Lamps",
    "5. Artist",
]

for dir_name in ASSET_DIRS:
    src_dir = ASSETS_DIR / dir_name
    if not src_dir.exists():
        continue

    thumbs_dir = src_dir / "thumbs"
    thumbs_dir.mkdir(exist_ok=True)

    for img_path in sorted(src_dir.glob("*.jpg")):
        thumb_path = thumbs_dir / img_path.name
        img = Image.open(img_path)
        img = ImageOps.exif_transpose(img)
        img.thumbnail((MAX_SIZE, MAX_SIZE), Image.LANCZOS)
        img.save(thumb_path, "JPEG", quality=QUALITY)
        size_kb = thumb_path.stat().st_size / 1024
        print(f"  {img_path.name} -> {img.size[0]}x{img.size[1]} ({size_kb:.0f}KB)")

print("Done.")
