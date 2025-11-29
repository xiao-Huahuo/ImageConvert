from PIL import Image

def bmp_to_webp(input_path, output_path):
    """Converts BMP to WebP."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'webp', quality=80)
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 BMP 转换为 WebP 时出错: {e}"

def webp_to_bmp(input_path, output_path):
    """Converts WebP to BMP."""
    try:
        img = Image.open(input_path)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'bmp')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 WebP 转换为 BMP 时出错: {e}"
