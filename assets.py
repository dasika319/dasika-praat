"""在打包机上自动生成应用图标和 DMG 背景图（PIL 绘制，无需上传图片）"""
import os
from PIL import Image, ImageDraw

os.makedirs("resources", exist_ok=True)

# ---- 1024x1024 应用图标：蓝色圆角底 + 白色麦克风 ----
size = 1024
icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
d = ImageDraw.Draw(icon)
for i in range(size):
    c = int(80 + 100 * i / size)
    d.line([(0, i), (size, i)], fill=(40, c, 220, 255))
mask = Image.new("L", (size, size), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, size - 1, size - 1], radius=180, fill=255)
icon.putalpha(mask)
d = ImageDraw.Draw(icon)
cx = size // 2
d.rounded_rectangle([cx-90, 200, cx+90, 480], radius=90, fill=(255, 255, 255, 255))
d.rectangle([cx-20, 480, cx+20, 560], fill=(255, 255, 255, 255))
d.arc([cx-160, 320, cx+160, 640], start=0, end=180, fill=(255, 255, 255, 255), width=28)
d.line([(cx-200, 600), (cx+200, 600)], fill=(255, 255, 255, 255), width=28)
icon.save("resources/app_icon.png")

# ---- 800x600 DMG 背景：拖向 Applications 的箭头 ----
bg = Image.new("RGB", (800, 600), (245, 246, 250))
d = ImageDraw.Draw(bg)
d.text((400, 60), "Install Voice Analysis Tool", anchor="mm", fill=(40, 60, 120))
d.text((200, 250), "Drag the app", anchor="mm", fill=(80, 90, 110))
d.text((600, 250), "into", anchor="mm", fill=(80, 90, 110))
d.line([(280, 320), (520, 320)], fill=(60, 130, 246), width=16)
d.polygon([(520, 290), (520, 350), (580, 320)], fill=(60, 130, 246))
d.text((400, 540), "Then open it from Applications", anchor="mm", fill=(120, 130, 150))
bg.save("resources/installer_bg.png")

print("✅ 图标与背景图已生成")
