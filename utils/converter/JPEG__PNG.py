from PIL import Image

def jpeg_to_png(input_path, output_path):
    """Converts JPEG to PNG."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'png')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 JPEG 转换为 PNG 时出错: {e}"

def png_to_jpeg(input_path, output_path):
    """Converts PNG to JPEG, handling transparency."""
    try:
        img = Image.open(input_path)
        # If the image has transparency, convert it to RGB
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'jpeg')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 PNG 转换为 JPEG 时出错: {e}"
