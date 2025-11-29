from PIL import Image

def ico_to_bmp(input_path, output_path):
    """Converts ICO to BMP."""
    try:
        img = Image.open(input_path)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'bmp')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 ICO 转换为 BMP 时出错: {e}"

def bmp_to_ico(input_path, output_path):
    """Converts BMP to ICO."""
    try:
        img = Image.open(input_path)
        sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(output_path, 'ico', sizes=sizes)
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 BMP 转换为 ICO 时出错: {e}"
