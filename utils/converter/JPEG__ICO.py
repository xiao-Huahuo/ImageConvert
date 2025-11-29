from PIL import Image

def jpeg_to_ico(input_path, output_path):
    """Converts JPEG to ICO."""
    try:
        img = Image.open(input_path)
        sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(output_path, 'ico', sizes=sizes)
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 JPEG 转换为 ICO 时出错: {e}"

def ico_to_jpeg(input_path, output_path):
    """Converts ICO to JPEG."""
    try:
        img = Image.open(input_path)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'jpeg')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 ICO 转换为 JPEG 时出错: {e}"
