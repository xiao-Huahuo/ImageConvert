from PIL import Image

def png_to_ico(input_path, output_path):
    """Converts PNG to ICO."""
    try:
        img = Image.open(input_path)
        sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(output_path, 'ico', sizes=sizes)
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 PNG 转换为 ICO 时出错: {e}"

def ico_to_png(input_path, output_path):
    """Converts ICO to PNG."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'png')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 ICO 转换为 PNG 时出错: {e}"
