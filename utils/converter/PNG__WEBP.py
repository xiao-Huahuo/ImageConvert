from PIL import Image

def png_to_webp(input_path, output_path):
    """Converts PNG to WebP."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'webp', quality=80)
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 PNG 转换为 WebP 时出错: {e}"

def webp_to_png(input_path, output_path):
    """Converts WebP to PNG."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'png')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 WebP 转换为 PNG 时出错: {e}"
