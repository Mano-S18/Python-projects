from PIL import Image, ImageFilter
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from credentials.cnfg import thumbnail

#Thumbnail
img = Image.open(thumbnail.source)
filtered_img = img.filter(ImageFilter.SHARPEN)
img.thumbnail((200, 200))
img.save(thumbnail.destination,'png')

