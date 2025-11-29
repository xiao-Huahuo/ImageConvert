from PIL import Image

def png_to_bmp(input_path, output_path):
    """Converts PNG to BMP."""
    try:
        img = Image.open(input_path)
        # BMP不支持透明度，所以需要转换为RGB
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'bmp')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 PNG 转换为 BMP 时出错: {e}"

def bmp_to_png(input_path, output_path):
    """Converts BMP to PNG."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'png')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 BMP 转换为 PNG 时出错: {e}"
